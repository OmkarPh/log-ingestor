package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"sync"
	"time"

	"github.com/elastic/go-elasticsearch/esapi"
	"github.com/elastic/go-elasticsearch/v8"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/segmentio/kafka-go"
)

// Log ingestion Configuration
const (
	logsBufferSize = 5000

	// Concurrent processing limit
	maxConcurrentLogs = 20

	// Kafka configuration
	kafkaBrokerHost = "localhost:9092"
)

// Kafka topics to consume from
var topics = []string{"auth", "database", "email", "payment", "server", "services"}

// Log structure
type Log struct {
	Level      string                 `json:"level"`
	Message    string                 `json:"message"`
	ResourceID string                 `json:"resourceId"`
	Timestamp  time.Time              `json:"timestamp"`
	TraceID    string                 `json:"traceId"`
	SpanID     string                 `json:"spanId"`
	Commit     string                 `json:"commit"`
	Metadata   map[string]interface{} `json:"metadata"`
}
type SavedLog struct {
	Log
	ParentResourceID string `json:"parentResourceId"`
}

// IngestionContext stores the Elasticsearch client and log channel information
type IngestionContext struct {
	esClient        *elasticsearch.Client
	indexName       string
	logChannel      chan Log
	workerWaitGroup sync.WaitGroup
}

func NewLogRequest(c *gin.Context, ingestionContext *IngestionContext) {
	var log Log
	if err := c.BindJSON(&log); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Bad Request"})
		return
	}

	// Send the log to the buffered channel for processing
	ingestionContext.logChannel <- log

	response := gin.H{
		"status": "success",
	}

	c.JSON(http.StatusAccepted, response)
}

func CountLogs(c *gin.Context, ingestionContext *IngestionContext) {
	// Use the Count API to get the count of logs in Elasticsearch
	countReq := esapi.CountRequest{
		Index: []string{ingestionContext.indexName},
	}

	res, err := countReq.Do(context.Background(), ingestionContext.esClient)
	if err != nil {
		fmt.Println("Error querying logs count from Elasticsearch:", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}
	defer res.Body.Close()

	if res.IsError() {
		fmt.Printf("Failed to get logs count from Elasticsearch. Response: %s\n", res.String())
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}

	var countResponse map[string]interface{}
	if err := json.NewDecoder(res.Body).Decode(&countResponse); err != nil {
		fmt.Println("Error decoding Elasticsearch count response:", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}

	// Extract the count from the response
	count, ok := countResponse["count"].(float64)
	if !ok {
		fmt.Println("Error extracting count from Elasticsearch response")
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"count": int(count)})
}

// Filter using combination of columns and values
type FilterCondition struct {
	ColumnName   string   `json:"columnName"`
	FilterValues []string `json:"filterValues"`
}

// TimeRange structure for specifying a time range
type TimeRange struct {
	StartTime time.Time `json:"startTime"`
	EndTime   time.Time `json:"endTime"`
}

// SearchParameters structure for specifying search parameters
type SearchParameters struct {
	Text      string            `json:"text"`
	Filters   []FilterCondition `json:"filters"`
	TimeRange TimeRange         `json:"timeRange"`
}

// Updated SearchLogs function to handle multiple filter values
func SearchLogs(c *gin.Context, ingestionContext *IngestionContext) {
	var searchParams SearchParameters
	if err := c.BindJSON(&searchParams); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Bad Request"})
		return
	}

	// Construct a search query based on the provided parameters
	var query string
	if searchParams.Text != "" {
		query = fmt.Sprintf("`%s`", searchParams.Text)
	}

	// Add filtering based on multiple columns and values
	for _, filter := range searchParams.Filters {
		if filter.ColumnName != "" && len(filter.FilterValues) > 0 {
			var columnQuery string
			for _, filterValue := range filter.FilterValues {
				if columnQuery == "" {
					columnQuery = fmt.Sprintf("%s:'%s'", filter.ColumnName, filterValue)
				} else {
					columnQuery = fmt.Sprintf("%s OR %s:'%s'", columnQuery, filter.ColumnName, filterValue)
				}
			}

			if query == "" {
				query = columnQuery
			} else {
				query = fmt.Sprintf("%s AND (%s)", query, columnQuery)
			}
		}
	}

	// Get logs in specified time range
	if !searchParams.TimeRange.StartTime.IsZero() && !searchParams.TimeRange.EndTime.IsZero() {
		timeQuery := fmt.Sprintf("timestamp:[%s TO %s]", searchParams.TimeRange.StartTime.Format(time.RFC3339), searchParams.TimeRange.EndTime.Format(time.RFC3339))
		if query == "" {
			query = timeQuery
		} else {
			query = fmt.Sprintf("%s AND %s", query, timeQuery)
		}
	}

	// If text is empty, consider all logs
	if query == "" {
		query = "*:*"
	}

	fmt.Printf("Query: ```%s``` \n", query)

	// Use the Search API to get logs from Elasticsearch
	searchReq := esapi.SearchRequest{
		Index: []string{ingestionContext.indexName},
		Body:  strings.NewReader(fmt.Sprintf(`{"query": {"query_string": {"query": "%s"}}, "size": 5000, "from": 0}`, query)),
	}

	res, err := searchReq.Do(context.Background(), ingestionContext.esClient)
	if err != nil {
		fmt.Println("Error querying logs from Elasticsearch:", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}
	defer res.Body.Close()

	if res.IsError() {
		fmt.Printf("Failed to get logs from Elasticsearch. Response: %s\n", res.String())
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}

	// Decode the response and send it as JSON
	var searchResponse map[string]interface{}
	if err := json.NewDecoder(res.Body).Decode(&searchResponse); err != nil {
		fmt.Println("Error decoding Elasticsearch search response:", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
		return
	}

	c.JSON(http.StatusOK, searchResponse)
}

// Setup ingestion & query routes
func setupRoutes(ingestionContext *IngestionContext) *gin.Engine {
	router := gin.Default()

	// Use the CORS middleware
	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"*"} // Allow all origins
	config.AllowMethods = []string{"GET", "POST", "PUT", "DELETE"}
	router.Use(cors.New(config))

	router.POST("/", func(c *gin.Context) { NewLogRequest(c, ingestionContext) })

	router.GET("/logs-count", func(ctx *gin.Context) { CountLogs(ctx, ingestionContext) })

	router.POST("/search-logs", func(c *gin.Context) { SearchLogs(c, ingestionContext) })

	return router
}

// saveLogWorker handles log processing
func saveLogWorker(ingestionContext *IngestionContext, workerID int) {
	defer ingestionContext.workerWaitGroup.Done()

	for log := range ingestionContext.logChannel {
		// Simulate processing time for testing
		// time.Sleep(500 * time.Millisecond)

		fmt.Printf("Worker %d processing log: %+v\n\n", workerID, log)

		// Check if "parentResourceId" is present in metadata
		var savedLog SavedLog
		savedLog.Log = log

		if parentID, ok := log.Metadata["parentResourceId"]; ok {
			// If present, add it to the SavedLog as "ParentResourceID" and remove from metadata
			if parentIDStr, ok := parentID.(string); ok {
				savedLog.ParentResourceID = parentIDStr
			}
		}

		// Index the log into Elasticsearch
		docJSON, err := json.Marshal(savedLog)
		if err != nil {
			fmt.Println("Error encoding log to JSON:", err)
			continue
		}

		req := esapi.IndexRequest{
			Index:      ingestionContext.indexName,
			DocumentID: "", // Elasticsearch will generate a document ID
			Body:       strings.NewReader(string(docJSON)),
			Refresh:    "true",
		}

		res, err := req.Do(context.Background(), ingestionContext.esClient)
		if err != nil {
			fmt.Println("Error indexing log into Elasticsearch:", err)
			continue
		}
		defer res.Body.Close()

		if res.IsError() {
			fmt.Printf("Failed to index log into Elasticsearch. Response: %s\n", res.String())
			continue
		}
	}
}

// KafkaConsumer consumes logs from Kafka
func KafkaConsumer(ingestionContext *IngestionContext, topics []string) {
	for _, topic := range topics {
		go func(topic string) {
			reader := kafka.NewReader(kafka.ReaderConfig{
				Brokers:  []string{kafkaBrokerHost},
				Topic:    topic,
				GroupID:  "log-consumer-group",
				MaxBytes: 10e6, // 10MB
			})

			defer reader.Close()

			for {
				message, err := reader.FetchMessage(context.Background())
				if err != nil {
					// fmt.Printf("Error fetching message from Kafka for topic %s: %v\n", topic, err)
					continue
				}

				var log Log
				err = json.Unmarshal(message.Value, &log)
				if err != nil {
					fmt.Printf("Error decoding log from Kafka message for topic %s: %v\n", topic, err)
					continue
				}

				// Send the log to the buffer channel for processing
				ingestionContext.logChannel <- log

				reader.CommitMessages(context.Background(), message)
			}
		}(topic)
	}
}

func main() {
	// Connect to Elasticsearch
	esConfig := elasticsearch.Config{
		Addresses: []string{"http://localhost:9200"},
	}
	esClient, err := elasticsearch.NewClient(esConfig)
	if err != nil {
		fmt.Println("Error creating Elasticsearch client:", err)
		return
	}

	ingestionContext := &IngestionContext{
		esClient:   esClient,
		indexName:  "log-ingestor",
		logChannel: make(chan Log, logsBufferSize),
	}

	// Start log processing workers
	for i := 1; i <= maxConcurrentLogs; i++ {
		ingestionContext.workerWaitGroup.Add(1)
		go saveLogWorker(ingestionContext, i)
	}

	// Start Kafka consumer with multiple topics
	go KafkaConsumer(ingestionContext, topics)

	router := setupRoutes(ingestionContext)

	fmt.Println("Starting server on :3000...")
	if err := router.Run(":3000"); err != nil {
		fmt.Println("Error starting server:", err)
	}

	fmt.Println("Bye !!!")

	// Close the log channel and wait for all workers to finish before exiting
	close(ingestionContext.logChannel)
	ingestionContext.workerWaitGroup.Wait()
}

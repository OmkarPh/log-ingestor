package main

import (
	"fmt"
	"sync"
	"time"

	"github.com/elastic/go-elasticsearch/v8"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

// Configuration
const (
	// Define number of logs to buffer before processing
	logsBufferSize = 5000

	// Concurrent processing limit
	maxConcurrentLogs = 20
)

// Kafka configuration
const kafkaBrokerHost = "localhost:9092"

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

// IngestionContext stores the Elasticsearch client and log channel information
type IngestionContext struct {
	esClient        *elasticsearch.Client
	indexName       string
	logChannel      chan Log
	workerWaitGroup sync.WaitGroup
}

// Setup ingestion & query routes
func setupRoutes(ingestionContext *IngestionContext) *gin.Engine {
	router := gin.Default()

	// Use the CORS middleware
	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"*"} // Allow all origins
	config.AllowMethods = []string{"GET", "POST", "PUT", "DELETE"}
	router.Use(cors.New(config))

	// Ingest logs
	router.POST("/", func(c *gin.Context) { NewLogRequest(c, ingestionContext) })

	// Query number of logs
	router.GET("/logs-count", func(ctx *gin.Context) { CountLogs(ctx, ingestionContext) })

	// Query logs
	router.POST("/search-logs", func(c *gin.Context) { SearchLogs(c, ingestionContext) })

	return router
}

func main() {
	// Elasticsearch connection
	esConfig := elasticsearch.Config{
		Addresses: []string{"http://localhost:9200"},
	}

	esClient, err := elasticsearch.NewClient(esConfig)
	if err != nil {
		fmt.Println("Error creating Elasticsearch client:", err)
		return
	}

	// Ingestion context
	ingestionContext := &IngestionContext{
		esClient:   esClient,
		indexName:  "log-ingestor",
		logChannel: make(chan Log, logsBufferSize),
	}

	// Register workers with independent goroutines for processing Logs
	for i := 1; i <= maxConcurrentLogs; i++ {
		ingestionContext.workerWaitGroup.Add(1)
		go saveLogWorker(ingestionContext, i)
	}

	// Start Kafka consumer in independent goroutine
	go KafkaConsumer(ingestionContext, topics)

	// Setup API routes
	router := setupRoutes(ingestionContext)

	// Start server
	fmt.Println("Starting server on :3000...")
	if err := router.Run(":3000"); err != nil {
		fmt.Println("Error starting server:", err)
	}

	// Close the log channel and wait for all workers to finish before exiting
	close(ingestionContext.logChannel)
	ingestionContext.workerWaitGroup.Wait()
}

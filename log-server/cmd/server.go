package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/segmentio/kafka-go"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

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

// LogStore is a MongoDB-backed store for logs
type LogStore struct {
	collection *mongo.Collection
	logCh      chan Log
	workerWG   sync.WaitGroup
}

const (
	bufferSize = 1000

	// Concurrent processing limit
	maxConcurrentLogs = 100

	// Kafka configuration
	kafkaBroker = "localhost:9092"
)

// Kafka configuration
var topics = []string{"auth", "database", "email", "payment", "server", "services"}

// Setup ingestion & query routes
func setupRouter(logStore *LogStore) *gin.Engine {
	r := gin.Default()

	r.POST("/", func(c *gin.Context) {
		var log Log
		if err := c.BindJSON(&log); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Bad Request"})
			return
		}

		// Send the log to the buffered channel for processing
		logStore.logCh <- log

		response := gin.H{
			"status": "success",
		}

		c.JSON(http.StatusAccepted, response)
	})

	r.GET("/logs-count", func(c *gin.Context) {
		count, err := logStore.collection.CountDocuments(context.TODO(), bson.D{})
		if err != nil {
			fmt.Println("Error querying logs count:", err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal Server Error"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"count": count})
	})

	return r
}

// LogWorker handles log processing
func logWorker(logStore *LogStore, workerID int) {
	defer logStore.workerWG.Done()

	for log := range logStore.logCh {
		// Simulate processing time for testing
		// time.Sleep(500 * time.Millisecond)

		fmt.Printf("Worker %d processing log: %+v\n\n", workerID, log)

		_, err := logStore.collection.InsertOne(context.TODO(), log)
		if err != nil {
			fmt.Println("Error inserting log into database:", err)
		}
	}
}

// KafkaConsumer consumes logs from Kafka
func KafkaConsumer(logStore *LogStore, topics []string) {
	for _, topic := range topics {
		go func(topic string) {
			reader := kafka.NewReader(kafka.ReaderConfig{
				Brokers:  []string{kafkaBroker},
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

				// Send the log to the buffered channel for processing
				logStore.logCh <- log

				reader.CommitMessages(context.Background(), message)
			}
		}(topic)
	}
}

func main() {
	// Connect to MongoDB
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		fmt.Println("Error creating MongoDB client:", err)
		return
	}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	err = client.Connect(ctx)
	if err != nil {
		fmt.Println("Error connecting to MongoDB:", err)
		return
	}
	defer client.Disconnect(ctx)

	// Specify the database and collection
	collection := client.Database("log-ingestor").Collection("logs")

	logStore := &LogStore{
		collection: collection,
		logCh:      make(chan Log, bufferSize),
	}

	// Start log processing workers
	for i := 1; i <= maxConcurrentLogs; i++ {
		logStore.workerWG.Add(1)
		go logWorker(logStore, i)
	}

	// Start Kafka consumer with multiple topics
	go KafkaConsumer(logStore, topics)

	r := setupRouter(logStore)

	fmt.Println("Starting server on :3000...")
	if err := r.Run(":3000"); err != nil {
		fmt.Println("Error starting server:", err)
	}

	fmt.Println("Bye !!!")

	// Close the log channel and wait for all workers to finish before exiting
	close(logStore.logCh)
	logStore.workerWG.Wait()
}

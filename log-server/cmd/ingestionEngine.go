package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/elastic/go-elasticsearch/esapi"
	"github.com/gin-gonic/gin"
)

// Number of logs to process in each batch
const batchSize = 10

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

// saveLogWorker handles log processing
func saveLogWorker(ingestionContext *IngestionContext, workerID int) {
	defer ingestionContext.workerWaitGroup.Done()

	var logsToInsert []Log

	for log := range ingestionContext.logChannel {
		logsToInsert = append(logsToInsert, log)

		// Check if we have collected enough logs or the channel is closed
		if len(logsToInsert) == batchSize || len(ingestionContext.logChannel) == 0 {
			// @TEST - Simulate processing time for testing
			// time.Sleep(500 * time.Millisecond)

			fmt.Printf("Worker %d processing logs: %+v\n\n", workerID, logsToInsert)

			// Index the logs into Elasticsearch in bulk
			var bulkRequestBody strings.Builder
			for _, log := range logsToInsert {
				// Each log should be a separate JSON object with its own index metadata
				indexMetadata := fmt.Sprintf(`{"index": {"_index": "%s"}}`, ingestionContext.indexName)
				logJSON, err := json.Marshal(log)
				if err != nil {
					fmt.Println("Error encoding log to JSON:", err)
					continue
				}
				bulkRequestBody.WriteString(indexMetadata)
				bulkRequestBody.WriteString("\n")
				bulkRequestBody.Write(logJSON)
				bulkRequestBody.WriteString("\n")
			}

			req := esapi.BulkRequest{
				Body:    strings.NewReader(bulkRequestBody.String()),
				Refresh: "true",
			}

			res, err := req.Do(context.Background(), ingestionContext.esClient)
			if err != nil {
				fmt.Println("Error indexing logs into Elasticsearch:", err)
				logsToInsert = nil
				continue
			}
			defer res.Body.Close()

			if res.IsError() {
				fmt.Printf("Failed to index logs into Elasticsearch. Response: %s\n", res.String())
				logsToInsert = nil
				continue
			}

			// Clear the logs slice
			logsToInsert = nil
		}
	}
}

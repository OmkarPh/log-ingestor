package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"

	"github.com/elastic/go-elasticsearch/esapi"
	"github.com/gin-gonic/gin"
)

// SearchParameters structure for specifying search parameters
type SearchParameters struct {
	Text      string            `json:"text"`
	RegexText string            `json:"regexText"`
	Filters   []FilterCondition `json:"filters"`
	TimeRange TimeRange         `json:"timeRange"`
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

	// Add regex search across all fields
	if searchParams.RegexText != "" {
		if query != "" {
			query += " AND "
		}
		query += fmt.Sprintf("`/.*%s.*/`", searchParams.RegexText)
	}

	// Add filtering based on multiple columns and values
	for _, filter := range searchParams.Filters {
		if filter.ColumnName != "" && len(filter.FilterValues) > 0 {
			var columnQuery string
			for _, filterValue := range filter.FilterValues {
				if columnQuery == "" {
					columnQuery = fmt.Sprintf("(%s:'%s'", filter.ColumnName, filterValue)
				} else {
					columnQuery = fmt.Sprintf("%s OR %s:'%s'", columnQuery, filter.ColumnName, filterValue)
				}
			}
			columnQuery = fmt.Sprintf("%s)", columnQuery)

			if query == "" {
				query = columnQuery
			} else {
				query = fmt.Sprintf("%s AND (%s)", query, columnQuery)
			}
		}
	}

	// Get logs in specified time range
	if !searchParams.TimeRange.StartTime.IsZero() || !searchParams.TimeRange.EndTime.IsZero() {
		var timeQuery string
		if !searchParams.TimeRange.StartTime.IsZero() && !searchParams.TimeRange.EndTime.IsZero() {
			// Both start and end times are provided
			timeQuery = fmt.Sprintf("timestamp:[%s TO %s]", searchParams.TimeRange.StartTime.Format(time.RFC3339), searchParams.TimeRange.EndTime.Format(time.RFC3339))
		} else if !searchParams.TimeRange.StartTime.IsZero() {
			// Only start time is provided
			timeQuery = fmt.Sprintf("timestamp:[%s TO *]", searchParams.TimeRange.StartTime.Format(time.RFC3339))
		} else {
			// Only end time is provided
			timeQuery = fmt.Sprintf("timestamp:[* TO %s]", searchParams.TimeRange.EndTime.Format(time.RFC3339))
		}

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

	fmt.Printf("Query: `%s` \n", query)

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

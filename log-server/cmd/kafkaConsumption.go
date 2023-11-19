package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/segmentio/kafka-go"
)

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

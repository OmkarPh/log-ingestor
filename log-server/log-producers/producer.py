import json
import time
import argparse
from kafka import KafkaProducer

LOGS_TIME_INTERVAL = 1  # Time interval between sending logs (in seconds)

TEST_LOGS_PATH = "logs"

log_level_topics = [
  "auth",
  "database",
  "email",
  "payment",
  "server",
  "services",
]

# Parse command line arguments
parser = argparse.ArgumentParser(description='Kafka producer with user-specified topic')
parser.add_argument('--topic', required=True, help='Kafka topic to produce logs to')
args = parser.parse_args()

# Kafka configuration (Local Kafka instance)
kafka_config = {
  "bootstrap_servers": "localhost:9092",
}

# Kafka producer obj
producer = KafkaProducer(**kafka_config)

# Concerned topic
topic = args.topic

# File to read and send lines from
file_path = f"{TEST_LOGS_PATH}/{topic}.json"

print(f"Producing logs to topic - {topic} ...\n")
print(f"File path: {file_path}")

# Read and send JSON objects from the file
with open(file_path, "r") as file:
    data = json.load(file)
    for json_object in data:
        message = json.dumps(json_object)
        producer.send(topic, message.encode("utf-8"))
        producer.flush()
        print(f"Produced ({topic}): {message}\n")
        time.sleep(LOGS_TIME_INTERVAL)  # Delay between sending messages

# # Close the producer
# producer.close()
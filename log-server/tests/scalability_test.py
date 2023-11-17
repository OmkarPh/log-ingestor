import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor
from sample_logs import sample_logs

PORT = 3000
LOGS_LENGTH = 300
BASE_URL = f"http://localhost:{PORT}"


# Repeat the sample_logs array as needed to reach or exceed the desired length n
logs = (sample_logs * (LOGS_LENGTH // len(sample_logs) + 1))[:LOGS_LENGTH]
random.shuffle(logs)

print("Logs:", len(logs))

# Get number of logs in the database
def get_logs_count():
    response = requests.get(f"{BASE_URL}/logs-count")
    if response.status_code == 200:
        log_count = response.json().get("count", 0)
        return log_count
    else:
        print(f"Error getting logs count: {response.text}")

# Make HTTP call to the put the log
def post_log(log_data):
    # print(f"Sent log")
    response = requests.post(f"{BASE_URL}/", json=log_data)
    if response.status_code != 202:
        print(f"Error sending log: {response.text}")

# Process all the logs
def scalability_tester():
    # Submit a new thread for posting each of the logs
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(post_log, logs)

    # Sleep for 2 seconds
    time.sleep(2)

if __name__ == "__main__":
    # Get the number of logs in the database at the beginning
    initial_log_count = get_logs_count()
    print(f"Number of logs in the database before ingestion: {initial_log_count}")
    
    print("Start ingesting the logs ......")

    # Process all the logs
    scalability_tester()

    print(f"Ingested {LOGS_LENGTH} logs successfuly !!")

    # Get the number of logs in the database after scalability_tester is complete
    post_test_log_count = get_logs_count()
    print(f"Number of logs in the database after ingestion: {post_test_log_count}")

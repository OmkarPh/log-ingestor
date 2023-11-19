import random
from datetime import datetime, timedelta

def generate_random_timestamp_in_range(start_date: datetime, end_date: datetime):
    random_days = random.randint(0, (end_date - start_date).days)
    random_time = timedelta(seconds=random.randint(0, 24*60*60 - 1))
    
    random_timestamp = start_date + timedelta(days=random_days) + random_time
    formatted_timestamp = random_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_timestamp

def generate_commit():
    commit = ''.join(random.choice('0123456789abcdef') for _ in range(7))
    return commit
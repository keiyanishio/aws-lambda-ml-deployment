import os
import requests
from dotenv import load_dotenv

load_dotenv()
endpoint = os.environ["API_ENDPOINT"]
payload = {
    "age": 42,
    "job": "entrepreneur",
    "marital": "married",
    "education": "primary",
    "balance": 558,
    "housing": "yes",
    "duration": 186,
    "campaign": 2,
}
response = requests.post(endpoint, json=payload, timeout=30)
print(response.status_code)
print(response.text)

import requests
import json

# Fetch data from SWAPI
response = requests.get("https://swapi.dev/api/people/1")
data = response.json()

# Send data to App2 using POST request
app2_url = "http://localhost:8000/receive"
headers = {"Content-Type": "application/json"}
response = requests.post(app2_url, data=json.dumps(data), headers=headers)

print("App1 sent data to App2 with response:", response.text)
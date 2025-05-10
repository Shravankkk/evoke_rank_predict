import requests

url = 'http://127.0.0.1:5000/calculate'

data = {
    "easy": 80,
    "medium": 60,
    "hard": 40,
    "marks": 300
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")









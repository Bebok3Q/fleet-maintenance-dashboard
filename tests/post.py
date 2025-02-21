import requests

url = "http://127.0.0.1:8000/api/vehicles/"
data = {
    "name": "Ford Focus",
    "vin": "1HGCM82633A123456",
    "mileage": 120000.5
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

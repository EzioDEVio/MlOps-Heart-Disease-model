import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = [
    {
        "age": 63,
        "sex": 1,
        "cp": 3,
        "trestbps": 145,
        "chol": 233,
        "fbs": 1,
        "restecg": 0,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 2.3,
        "slope": 3,
        "ca": 0,
        "thal": 6
    }
]

response = requests.post(url, json=data)
print(response.json())

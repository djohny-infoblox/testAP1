import requests
import json

BASE = "http://127.0.0.1:5000/"


data = requests.get(BASE + "hello/dhan")
print(data.json())
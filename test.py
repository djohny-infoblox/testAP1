import requests
import json
url = "http://127.0.0.1:5000/"

data = requests.get(url).json()
print(data)
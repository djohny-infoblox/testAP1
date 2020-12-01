import requests
import json

BASE = "http://15.236.19.165:30006/"


data = requests.get(BASE + "/coredns/health")
dd = data.json()
print (dd)

data = requests.get(BASE + "/coredns/readiness")
dd = data.json()
print (dd)

data = requests.get(BASE + "/grafana/health")
dd = data.json()
print (dd)

data = requests.get(BASE + "/influxdb/health")
dd = data.json()
print (dd)

data = requests.get(BASE + "/firefox/health")
dd = data.json()
print (dd)






    
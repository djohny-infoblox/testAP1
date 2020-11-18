from flask import Flask
from flask_restful import Api, Resource
from influxdb import InfluxDBClient
import time
import datetime
import requests

app = Flask(__name__)
api = Api(app)

names = {
         "tim":{"age":12,"place":"dfsdf"},
         "dhan":{"age":144,"place":"zzz"},
         }

# class helloworld(Resource):
#     def get(self,name):
#         return names[name]
#     def post(self):
#         return {"data" : "hello poasdsdsado"}
        
class coredns(Resource):
    def get(self):
        self.url = "http://15.236.19.165:8080/health"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"data":self.ee}

class coredns_ready(Resource):
    def get(self):
        self.url = "http://15.236.19.165:8181/ready"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"data":self.ee}

class csp_grafana(Resource):
    def get(self):
        self.url = "http://15.236.19.165:30003"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"data":self.ee}

class influxdb(Resource):
    def get(self):
        self.url = "http://15.236.19.165:30005/ping?wait_for_leader=30s"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"data":self.ee}


api.add_resource(coredns, "/coredns/health")
api.add_resource(coredns_ready, "/coredns/readiness")
api.add_resource(csp_grafana, "/grafana/health")
api.add_resource(influxdb, "/influxdb/health")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
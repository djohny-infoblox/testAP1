from flask import Flask
from flask_restful import Api, Resource
from influxdb import InfluxDBClient
import requests


app = Flask(__name__)
api = Api(app)

      
class coredns(Resource):
    def get(self):
        self.url = "http://15.236.19.165:8080/health"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"message":self.ee}

class coredns_ready(Resource):
    def get(self):
        self.url = "http://15.236.19.165:8181/ready"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"message":self.ee}

class csp_grafana(Resource):
    def get(self):
        self.url = "http://15.236.19.165:30003"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"message":self.ee}

class db(Resource):
    def get(self):
        self.url = "http://15.236.19.165:30005/ping?wait_for_leader=30s"
        self.res = requests.head(self.url)
        self.ee = str(self.res.status_code)
        return {"message":self.ee}

class firefox1(Resource):
    def get(self):
        self.url = "http://15.236.19.165:30004/wd/hub/status"
        self.res = requests.get(self.url)
        self.ee = str(self.res.status_code)
        return {"message":self.ee}
        

api.add_resource(coredns, "/coredns/health")
api.add_resource(coredns_ready, "/coredns/readiness")
api.add_resource(csp_grafana, "/grafana/health")
api.add_resource(db, "/influxdb/health")
api.add_resource(firefox1, "/firefox/health")



if __name__ == "__main__":
    app.run(host = "0.0.0.0")

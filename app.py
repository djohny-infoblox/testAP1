from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
         "tim":{"age":12,"place":"dfsdf"},
         "dhan":{"age":144,"place":"zzz"},
         }

class helloworld(Resource):
    def get(self,name):
        return names[name]
    def post(self):
        return {"data" : "hello poasdsdsado"}


api.add_resource(helloworld, "/hello/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
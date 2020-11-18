from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
    def get(self,name):
        return {"name" : name, "test":"test" }
    def post(self):
        return {"data" : "hello poasdsdsado"}


api.add_resource(helloworld, "/hello/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
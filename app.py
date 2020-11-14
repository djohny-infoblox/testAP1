from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
    def get(self):
        return {"data" : "hello dhkasdfaksdfkbsadjklfds"}

api.add_resource(helloworld, "/hello")

if __name__ == "__main__":
    app.run(debug=True)
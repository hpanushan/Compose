from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about':'hello world'}, 200

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

class New(Resource):
    def get(self,category,phrase):
        if category==1:
            modifiedPhase = phrase.replace('+',' ')
            return {"out":modifiedPhase}, 200

# Routes
api.add_resource(HelloWorld,'/')
api.add_resource(New,'/new/<int:category>/<string:phrase>')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class New(Resource):
    def get(self):
        # Activation
        return {"similarPhrase":12}, 200

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201

# Routes
api.add_resource(New,'/')

if __name__ == '__main__':
    app.run(port='5001',debug=True)
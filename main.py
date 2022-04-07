from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

sheldue = {
	1: {"day": "monday", "lessons": "russian_language, literature, biology, math, geography, history"}, 
	2: {"day": "tuesday", "lessons": "english, russian_language, pe, math, technology, physics"},
	3: {"day": "wednesday", "lessons": "russian_language, russian_literature, biology, geography, math, information_technology, art"},
	4: {"day": "thursday", "lessons": "russian_language, literature, information_technology, english, geometry, physics, pe"},
	5: {"day": "friday", "lessons": "geometry, pe, english, technology, history, social_studies, music"}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("ingredients", type=str)

class Main(Resource):
	def get(self, sheldue_id):
		if sheldue_id == 0:
			return sheldue
		else:
			return sheldue[sheldue_id]

	def delete(self, sheldue_id):
		del sheldue[sheldue_id]
		return sheldue


	def post(self, sheldue_id):
		sheldue[sheldue_id] = parser.parse_args()
		return sheldue

	def put(self, sheldue_id):
		sheldue[sheldue_id] = parser.parse_args()
		return sheldue

api.add_resource(Main, "/api/v1/lessons/<int:sheldue_id>")
api.init_app(app)

if __name__ == "__main__":
	app.run(debug=False, port=3000, host="127.0.0.1")
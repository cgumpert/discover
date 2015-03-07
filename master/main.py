#!/bin/python2

from flask import Flask, request
from flask.ext.restful import Resource, Api, reqparse
from Location import Location
app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return 'Hello'

class Push(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('x', type=float)
        parser.add_argument('y', type=float)
        parser.add_argument('time', type=int)
        parser.add_argument('intensity', type=float)

        args = parser.parse_args()

        location = Location(args['x'], args['y'])
        time = args['time']
        intensity = args['intensity']

        print(location.x)
        print(time)
        print(intensity)

api.add_resource(Hello, '/')
api.add_resource(Push, '/new')

if __name__ == "__main__":
    app.run(debug=True)


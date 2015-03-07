#!/bin/python2
import sys
sys.path.append("../")

from flask import Flask, request, render_template
from flask.ext.restful import Resource, Api, reqparse
from Location import Location
from Event import Event
from flask_socketio import SocketIO, emit
from geojson import Point, dumps

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
socketio = SocketIO(app)

events = {}

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/ws')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected')

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

        event = Event(location, time, intensity)

        socketio.emit('data', event.__geo_interface__, namespace='/ws')

        print(event.__geo_interface__)
        return "Success"

class Update(Resource):
    def post(self):
        return "OK"

api.add_resource(Push, '/new')
api.add_resource(Update, '/update')

if __name__ == "__main__":
    socketio.run(app)


#!/bin/python2
import sys
sys.path.append("../")

from flask import Flask, request, render_template
from flask.ext.restful import Resource, Api, reqparse
from Location import Location
from flask_socketio import SocketIO, emit

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
socketio = SocketIO(app)

@app.route("/")
def hello():
        return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
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

        print("Event in ({}:{}) at {} with {}".format(location.x, location.y, time, intensity))
        return "Success"

api.add_resource(Push, '/new')

if __name__ == "__main__":
    socketio.run(app)


#!/bin/python2
import sys
sys.path.append("../")

from flask import Flask, request, render_template
from flask.ext.restful import Resource, Api, reqparse
from Location import Location
from Event import Event
from flask_socketio import SocketIO, emit
from geojson import Point, FeatureCollection, dumps
import pickle

#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
socketio = SocketIO(app)

events = []
rec_events = []
rec_idx = 0

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
        global events
        parser = reqparse.RequestParser()
        parser.add_argument('x', type=float)
        parser.add_argument('y', type=float)
        parser.add_argument('time', type=int)
        parser.add_argument('intensity', type=float)
        parser.add_argument('id', type=int)

        args = parser.parse_args()

        location = Location(args['x'], args['y'])
        time = args['time']
        intensity = args['intensity']
        id = args['id']

        event = Event(location, time, intensity, id)
        events.append(event)

        return "Success"

class Update(Resource):
    def post(self):
        global events
        global rec_events
        global rec_idx
        parser = reqparse.RequestParser()
        parser.add_argument('recordTarget', type=str)
        parser.add_argument('recordReplay', type=str)
        args = parser.parse_args()
        recordTarget = args['recordTarget']
        recordReplay = args['recordReplay']
        
        #print("Update")
        #print(FeatureCollection(events))
        #socketio.emit('data', events[0].__geo_interface__, namespace='/ws')

        if recordReplay != "":
            #events = getEventsFromPickle(recordReplay).next()
            if rec_events == []:
                f_in = open(recordReplay, 'rb')
                while True:
                    try:
                        rec_events.append(pickle.load(f_in))
                    except EOFError:
                        break
                f_in.close()
            else:
                events = rec_events[rec_idx]
                if rec_idx == len(rec_events)-1:
                    rec_idx = 0
                else:
                    rec_idx += 1
            
        features = FeatureCollection(events)
        #print(features)
        socketio.emit('data', dumps(features), namespace='/ws')

        # dump to pickle
        if recordTarget != "":
            pickle.dump(events, open(recordTarget, "ab"))
        
            
        events = []
        return "OK"


def getEventsFromPickle(f_name):
    f_in = open(f_name, 'rb')
    for obj in f_in:
        yield pickle.load(f_in)
    
api.add_resource(Push, '/new')
api.add_resource(Update, '/update')

if __name__ == "__main__":
    socketio.run(app)


from Location import Location
from geojson import Point

class Event:
    def __init__(self, location = Location(0, 0), time = 0, intensity = 0.0, id = 0):
        self._location = location
        self._time = time
        self._intensity = intensity
        self._id = id

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def intensity(self):
        return self._intensity

    @time.setter
    def intensity(self, value):
        self._intensity = value

    @property
    def intensity(self):
        return self._id

    @time.setter
    def id(self, value):
        self._id = value


    def __str__(self):
        return "Event in ({}:{}) at {} with {}".format(self._location.x, self._location.y, self._time, self._intensity)

    @property
    def __geo_interface__(self):
        point = Point((self._location.x, self._location.y))
        return {'type': 'Feature', 'properties': {'intensity': self._intensity}, 'geometry': point.__geo_interface__, 'id': self._id}


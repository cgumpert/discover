from __future__ import division
from Location import Location
from functools import partial
from utility import gaussian, gps_dist_m, gps_delta_x
import math


class ShowerGenerator(object):
    def __init__(self, loc0, h0, angle, sigma, dt):
        self._alpha = angle
        self._time = 0
        self._loc0 = loc0
        self._h0 = h0
        self._c = 3e8
        self._dt = dt
        self._sigma = sigma
        self._duration = self.transform_time(math.sqrt((self._h0*math.tan(self._alpha))**2 + self._h0**2)/self._c)


    def transform_time(self, t):
        return t - self._h0/self._c

        
    def distance_to_shower_start(self, location):
        return math.sqrt(gps_dist_m(location, self._loc0)**2 + self._h0**2)


    def angle_to_shower_axis(self, location):
        return math.acos((gps_delta_x(location-self._loc0)*(h0*math.tan(self._alpha))+self._h0**2)/(self.distance_to_shower_start(location)*self._h0/math.cos(self._alpha)))

        
    def in_time_interval(self, location):
        t = self.distance_to_shower_start(location)/self._c 
        return self.transform_time(self._time) < t and self.transform_time(self._time + self._dt) > t
        

    def prob_density(self, location):
        if self.in_time_interval(location):
            return gaussian(self.angle_to_shower_axis(location), self._sigma)
        
        
    def nextStep(self):
        if self._time > self._duration + 1:
            return None
        self._time += self._dt
        return lambda loc: (self.prob_density(loc), 0.4*loc.y)
        

class SignalInjector(object):
    def __init__(self):
        self._showers = []

    def getSignal(self):
        return [shower for shower in [shower.nextStep() for shower in self._showers] if shower is not None]
            
    def startShower(self, loc0, h0, angle, sigma, dt):
        self._showers.append(ShowerGenerator(loc0, h0, angle, sigma, dt))

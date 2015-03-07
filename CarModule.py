################################################################################
# Implementation of Car Module
################################################################################

# python include(s)
import httplib, urllib
import random

# package include(s)
from Clock import clock


################################################################################
class Car(object):
    #_______________________________________ 
    def __init__(self, idx, location, rel_res = 0.1):
        self.__location = location
        self.__rel_res = rel_res
        self.__id = idx

    #_______________________________________ 
    def __str__(self):
        return "Car({0},{1},{2})".format(self.__id,
                                         self.__location.x,
                                         self.__location.y)
    
    #_______________________________________ 
    def __repr__(self):
        return self.__str__()
    
    #_______________________________________ 
    def getID(self):
        return self.__id

    #_______________________________________ 
    def updateID(self, value):
        self.__id = value
    
    #_______________________________________ 
    def getLocation(self):
        return self.__location

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location

    #_______________________________________ 
    def receiveSignal(self, intensity):
        intensity = self.__smearIntensity(intensity)
        intensity = self.__saturateIntensity(intensity)
        self.__postSignal(intensity)
        #print "Got Signal: {}".format(intensity)

    #_______________________________________ 
    def __smearIntensity(self, intensity):
        return random.gauss(intensity, intensity*self.__rel_res)
    
    #_______________________________________ 
    def __saturateIntensity(self, intensity):
        if intensity > 1:
            return 1
        else:
            return intensity

    #_______________________________________ 
    def __postSignal(self, intensity):
        package = {"id": self.__id,
                   "x": self.__location.x,
                   "y": self.__location.y,
                   "time": clock.time,
                   "intensity": intensity}

        # http server
        conn = httplib.HTTPConnection("localhost:5000")
        url = "/new"
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn.request("POST", url, urllib.urlencode(package),headers)
        r1 = conn.getresponse()
        if r1.reason != "OK":
            print "error during HTTP request: %s" % r1.reason
        conn.close()





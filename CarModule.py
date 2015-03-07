################################################################################
# Implementation of Car Module
################################################################################

# python include(s)
import httplib

# package include(s)
from Clock import clock


################################################################################
class Car(object):
    #_______________________________________ 
    def __init__(self, location):
        self.__location = location

        # http server
        self.__conn = httplib.HTTPConnection("localhost:5000")
        self.__url = "/new"


    #_______________________________________ 
    def __str__(self):
        return "Car({0},{1})".format(self.__location.x,
                                     self.__location.y)
    
    #_______________________________________ 
    def __repr__(self):
        return self.__str__()
    
    #_______________________________________ 
    def getLocation(self):
        return self.__location

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location

    #_______________________________________ 
    def receiveSignal(self, intensity):
        intensity = self.__saturateIntensity(intensity)
        self.__postSignal(intensity)
        #print "Got Signal: {}".format(intensity)

    #_______________________________________ 
    def __saturateIntensity(self, intensity):
        if intensity > 1:
            return 1
        else:
            return intensity

    #_______________________________________ 
    def __postSignal(self, intensity):
        package = {"x": self.__location.x,
                   "y": self.__location.y,
                   "time": clock.time(),
                   "intensity": intensity}

        self.__conn.request("POST", self.__url, package)





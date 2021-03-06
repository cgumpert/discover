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
    def __init__(self, idx, location, rel_res = 0.1, eff = 0.8):
        self.__location = location
        self.__rel_res = rel_res
        self.__eff = eff
        self.__id = idx

        # http server
        self.__conn = httplib.HTTPConnection("localhost:5000")
        self.__url = "/new"
        self.__headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"} 

    
    #_______________________________________ 
    def __del__(self):
        self.__conn.close()

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
    def getEff(self):
        return self.__eff

    #_______________________________________ 
    def updateEff(self, value):
        self.__eff = value

    #_______________________________________ 
    def getLocation(self):
        return self.__location

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location

    #_______________________________________ 
    def receiveSignal(self, intensity):
        intensity = self.__checkEff(intensity)
        intensity = self.__smearIntensity(intensity)
        intensity = self.__saturateIntensity(intensity)
        self.__postSignal(intensity)
        #print "Got Signal: {}".format(intensity)

    #_______________________________________ 
    def __checkEff(self, intensity):
        rdn = random.random()
        if rdn <= self.__eff:
            return intensity
        else:
            return 0
    
    #_______________________________________ 
    def __smearIntensity(self, intensity):
        if intensity > 0:
            intensity = random.gauss(intensity, intensity*self.__rel_res)
            if intensity < 0: intensity == 0
            return intensity
        else: 
            return 0

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
        self.__conn.request("POST", 
                            self.__url, 
                            urllib.urlencode(package), 
                            self.__headers)
        r1 = self.__conn.getresponse()
        r1.read()
        if r1.reason != "OK":
            print "Error during HTTP request: %s" % r1.reason
        
        #conn = httplib.HTTPConnection("localhost:5000")
        #url = "/new"
        #headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        #conn.request("POST", url, urllib.urlencode(package),headers)
        #r1 = conn.getresponse()
        #if r1.reason != "OK":
        #    print "error during HTTP request: %s" % r1.reason
        #conn.close()





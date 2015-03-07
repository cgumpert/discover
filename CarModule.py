################################################################################
# Implementation of Car Module
################################################################################

# python include(s)

# package include(s)
from Clock import clock


################################################################################
class Car(object):
    #_______________________________________ 
    def __init__(self, location, intensity = 0):
        self.__location = location

    #_______________________________________ 
    def __str__(self):
        return "Car({0},{1},{2})".format(self.__location.x,
                                         self.__location.y)
    
    #_______________________________________ 
    def __repr__(self):
        return self.__str__()
    
    #_______________________________________ 
    def getLocation(self): return self.__location

    #_______________________________________ 
    def receiveSignal(self, intensity):
        print "Got Signal: {}".format(intensity)

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location
    


################################################################################
# Implementation of Car Module
################################################################################

# python include(s)

# package include(s)
from Location import Location


################################################################################
class Car(object):
    #_______________________________________ 
    def __init__(self):
        self.__location = Location()
        self.__intensity = None

    #_______________________________________ 
    def getLocation(self): return self.__location
    def getIntensity(self): return self.__intensity

    #_______________________________________ 
    def receiveSignal(self, intensity):
        self.__intensity = intensity

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location
    
    #_______________________________________ 



################################################################################
# Implementation of Car Module
################################################################################

# python include(s)

# package include(s)


################################################################################
class Car(object):
    #_______________________________________ 
    def __init__(self, location, intensity = 0):
        self.__location = location
        self.__intensity = intensity

    #_______________________________________ 
    def __str__(self):
        return "Car({0},{1},{2})".format(self.__location.x,
                                         self.__location.y,
                                         self.__intensity)
    
    #_______________________________________ 
    def __repr__(self):
        return self.__str__()
    
    #_______________________________________ 
    def getLocation(self): return self.__location
    def getIntensity(self): return self.__intensity

    #_______________________________________ 
    def receiveSignal(self, intensity):
        self.__intensity = intensity

    #_______________________________________ 
    def updateLocation(self, location):
        self.__location = location
    


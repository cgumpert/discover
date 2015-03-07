# python include(s)
import random
import geopy
import geopy.distance

# package include(s)
from Location import Location

################################################################################
class LocationFinder(object):
    #_______________________________________ 
    def __init__(self):
        self.__min_distance = 100   # in meter
        self.__precision = 4
    
    ########################################        
    # Main API
    ######################################## 
    
    #_______________________________________ 
    def createRndLocations(self, nPoints = 100,
                                 south = 50.9591,
                                 west = 13.5770,
                                 north = 51.1024,
                                 east = 13.8963):
        
        result = []

        for idx in range(nPoints):
            tmp = Location( self.__getRndPoint(west, east),
                            self.__getRndPoint(south, north))

            if self.__noOverlapp(tmp, result):
                result.append(tmp)

        return result
    
    #_______________________________________ 
    def __getRndPoint(self, low, high):
        return round( random.uniform(low, high), self.__precision )
    
    #_______________________________________ 
    def __noOverlapp(self, location, loclist):
        for refLoc in loclist:
            pt1 = geopy.Point(location.x, location.y)
            pt2 = geopy.Point(refLoc.x, refLoc.y)

            dist = geopy.distance.distance(pt1, pt2).m
            if dist <= self.__min_distance:
                return False

        return True

    
    #_______________________________________ 
    
    
    ########################################        
    # Getter / Setter
    ######################################## 
    
    #_______________________________________ 
    @property
    def minDistance(self):
        return self.__min_distance
   
    #_______________________________________ 
    @minDistance.setter
    def minDistance(self, value):
        self.__min_distance = value

    #_______________________________________ 
    @property
    def precision(self):
        return self.__precision

    #_______________________________________ 
    @precision.setter
    def precision(self, value):
        if value < 0: value = abs(value)
        self.__precision = int(value)






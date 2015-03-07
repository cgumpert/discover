# python include(s)
import random, pickle
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
   
        # cache
        self.__streets = None


    ########################################        
    # Random Points
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

    ########################################        
    # Get points in streets
    ######################################## 
    #_______________________________________ 
    def queryStreets(self, south = 50.9591,
                           west = 13.5770,
                           north = 51.1024,
                           east = 13.8963):
        
        query_string = "way({0},{1},{2},{3}) [\"highway\"];(._;>;); out body;"
        import overpy
        api = overpy.Overpass()

        print "LocationFinder - Perform Query..."
        self.__streets =  api.query(query_string.format(south, west, north, east))
        print "LocationFinder - Query done..."

    #_______________________________________ 
    def createRndStreetLocations(self, nPoints = 100, pickle_output_file = None):
        if self.__streets == None:
            print "No street database found, run queryStreets first"
            return []

        if nPoints > len(self.__streets.ways):
           nPoints = len(self.__streets.ways) / 2

        location_list = []
        used_idx_pairs = []
        for i in range(0, nPoints):
            print "Get point number {}".format(i)
            loc, idx_pair = self.__getRndLocFromStreets()
            if not idx_pair in used_idx_pairs:
                used_idx_pairs.append(idx_pair)
                location_list.append(loc)

        if pickle_output_file:
            print "Save result as 'location_list' in {}".format(pickle_output_file)
            pickle.dump( location_list, open( pickle_output_file, "wb" ) )

        return location_list
    
    #_______________________________________ 
    def loadLocationListFromPickle(self, pickle_input_file):
        return pickle.load( open( pickle_input_file, "rb" ) )
    
    #_______________________________________ 
    def __getRndLocFromStreets(self):
        nWays = len(self.__streets.ways)
        way_idx = random.randint(0,nWays-1)
        way = self.__streets.ways[way_idx]

        nNodes = len(way.nodes)
        node_idx = random.randint(0,nNodes-1)
        node = way.nodes[node_idx]

        return Location(float(node.lon), float(node.lat)), [way_idx, node_idx]
    
    #_______________________________________ 
    #def __getFullLocList(self):
    #    l = []
    #    for way in self.__streets.ways:
    #        for node in way.nodes:
    #            l.append(Location(float(node.lon), float(node.lat)))
    #
    #    return l
    

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

    #_______________________________________ 
    @property
    def streets(self):
        return self.__streets
    
    #_______________________________________ 
    @streets.setter
    def streets(self, value):
        self.__streets = value





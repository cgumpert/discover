import math
from Location import Location
import geopy
import geopy.distance

def gaussian(x, sigma, mu = 0):
    return 1./math.sqrt(2*np.pi* sigma**2)*math.exp(-(x-mu)**2/(2*sigma**2))


def gps_dist_m(loc1, loc2):
    pt1 = geopy.Point(loc1.x, loc1.y)
    pt2 = geopy.Point(loc2.x, loc2.y)
    return geopy.distance.distance(pt1, pt2).m


def gps_delta_x(loc1, loc2):
    # https://stackoverflow.com/questions/3809179/angle-between-2-gps-coordinates
    # dy = loc2.y - loc1.y
    dx = math.cos(math.pi/180*loc1.y)*(loc2.x - loc1.x)
    # angle = atan2f(dy, dx)
    return math.abs(dx)

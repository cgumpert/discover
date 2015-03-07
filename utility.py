import math
from Location import Location
import geopy
import geopy.distance

def gps_to_ecef(loc):
    latitude = math.pi/180 * loc.y
    longitude = math.pi/180 * loc.x
    r = 6371000
    x = r * math.sin(latitude) * math.cos(longitude)
    y = r * math.sin(latitude) * math.sin(longitude)
    z = r * math.cos(latitude)
    return x,y,z

def ecef_to_enu(x_p,y_p,z_p,x_r,y_r,z_r):
    lambda_r = math.atan(y_r / x_r)
    phi_r = z_r / math.sqrt(x_r**2 + y_r**2)
    x = -math.sin(lambda_r) * (x_p - x_r) + math.cos(lambda_r) * (y_p - y_r)
    y = -math.sin(phi_r) * math.cos(lambda_r) * (x_p - x_r) - math.sin(phi_r) * math.sin(lambda_r) * (y_p - y_r) + math.cos(phi_r) * (z_p - z_r)
    return x,y

def gps_to_enu(loc,ref):
    x_p, y_p, z_p = gps_to_ecef(loc)
    x_r, y_r, z_r = gps_to_ecef(ref)
    return ecef_to_enu(x_p,y_p,z_p,x_r,y_r,z_r)

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

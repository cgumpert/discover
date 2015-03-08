import math
from Location import Location
import geopy
import geopy.distance


def gps_to_ecef(loc):
    latitude = - math.pi/180 * (loc.y - 90)
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
    z = math.cos(phi_r)*math.cos(lambda_r)*(x_p-x_r)+math.cos(phi_r)*math.sin(lambda_r)*(y_p-y_r)+math.sin(phi_r)*(z_p-z_r)
    return x, y, z


def enu_to_ecef(x_p, y_p, z_p, x_r, y_r, z_r):
    lambda_r = math.atan(y_r / x_r)
    phi_r = z_r / math.sqrt(x_r**2 + y_r**2)
    x = -math.sin(lambda_r)*x_p - math.sin(phi_r)*math.cos(lambda_r)*y_p +math.cos(phi_r)*math.cos(lambda_r)*z_p + x_r
    y = math.cos(lambda_r)*x_p -math.sin(phi_r)*math.sin(lambda_r)*y_p+math.cos(phi_r)*math.sin(lambda_r)*z_p + y_r
    z = math.cos(phi_r)*y_p + math.sin(phi_r)*z_p + z_r
    return x, y, z


def ecef_to_gps(x, y, z):
    theta = math.acos(z/math.sqrt(x**2+y**2+z**2))*180/math.pi
    phi = math.atan2(y, x)*180/math.pi
    return Location(phi, -1 * (theta - 90))


def enu_to_gps(x_p, y_p, z_p, ref):
    x_r, y_r, z_r = gps_to_ecef(ref)
    x, y, z = enu_to_ecef(x_p, y_p, z_p, x_r, y_r, z_r)
    return ecef_to_gps(x, y, z)
    
    
def gps_to_enu(loc,ref):
    x_p, y_p, z_p = gps_to_ecef(loc)
    x_r, y_r, z_r = gps_to_ecef(ref)
    return ecef_to_enu(x_p,y_p,z_p,x_r,y_r,z_r)

    
def gaussian(x, sigma, mu = 0):
    return math.exp(-(x-mu)**2/(2*sigma**2))


def gps_dist_m(loc1, loc2):
    #pt1 = geopy.Point(loc1.x, loc1.y)
    #pt2 = geopy.Point(loc2.x, loc2.y)
    #return geopy.distance.distance(pt1, pt2).m
    x, y, z = gps_to_enu(loc1, loc2)
    return math.sqrt(x**2+y**2)

def gps_delta_x(loc1, loc2):
    x1, _, _ = gps_to_enu(loc1, loc1)
    x2, _, _ = gps_to_enu(loc2, loc1)
    return x1-x2


def rotate_around_ref(location, ref, phi):
    x, y, z = gps_to_enu(location, ref)
    x_rot = math.cos(phi)*x - math.sin(phi)*y
    y_rot = math.sin(phi)*x + math.cos(phi)*y
    return enu_to_gps(x_rot, y_rot, z, ref)

import sys
import httplib, urllib
from CarHandlerModule import CarHandler
from Location import Location
from LocationFinder import LocationFinder
from SignalInjector import SignalInjector
from BackgroundInjector import BackgroundInjector
from Clock import clock
import time
import math

def update_server(recordTarget = "", recordReplay = ""):
    conn = httplib.HTTPConnection("localhost:5000")
    package = {"recordTarget": recordTarget, "recordReplay": recordReplay}
    header = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    url = "/update"
    conn.request("POST", url,
                 urllib.urlencode(package),
                 header)
    conn.getresponse()
    conn.close()
    
def main(argv):

    doRecord = ""
    doReplay = ""
    
    
    car_handler = CarHandler()
    loc_finder = LocationFinder()
    #car_handler.initialise( loc_finder.createRndLocations(300) )
    car_handler.initialise( loc_finder.loadLocationListFromPickle("share/locationList1000.p") )

    sig_injector = SignalInjector()
    bgk_injector = BackgroundInjector(threshold=0.4)
    clock.setEnd(1000)
    for _ in clock:
        if doReplay != "":
            update_server(doRecord, doReplay)
            time.sleep(0.5)
            continue
        if clock.time == 1:
            sig_injector.startShower(loc0 = Location(13.735, 51.04),
                                     h0 = 25000,
                                     phi = 0.,
                                     angle = 0.,
                                     sigma = 0.3,
                                     dt = 3e-7)
        if clock.time == 30:
            sig_injector.startShower(loc0 = Location(13.78, 51.04),
                                     h0 = 25000,
                                     phi = 0.,
                                     angle = math.pi/6,
                                     sigma = 0.5,
                                     dt = 3e-7)

            
        signals = sig_injector.getSignal()
        background = bgk_injector.getBackground()
        combine = [background]+signals
        car_handler.receiveSignal(*combine)
        update_server()
    

if __name__ == "__main__":
    main(sys.argv[1:])

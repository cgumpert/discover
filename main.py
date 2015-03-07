import sys
import httplib
from CarHandlerModule import CarHandler
from Location import Location
from LocationFinder import LocationFinder
from SignalInjector import SignalInjector
from BackgroundInjector import BackgroundInjector
from Clock import clock

def update_server():
    conn = httplib.HTTPConnection("localhost:5000")
    url = "/update"
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn.request("POST", url)
    conn.getresponse()
    conn.close()
    
def main(argv):
    car_handler = CarHandler()
    loc_finder = LocationFinder()
    car_handler.initialise( loc_finder.createRndLocations() )

    sig_injector = SignalInjector()
    bgk_injector = BackgroundInjector()
    clock.setEnd(100)
    for _ in clock:
        if clock.time == 10:
            sig_injector.startShower(loc0 = Location(51, 13.7),
                                     h0 = 25000,
                                     angle = 0.3,
                                     sigma = 0.03,
                                     dt = 1e-6)
                         
        signals = sig_injector.getSignal()
        background = bgk_injector.getBackground()
        combine = [background]+signals
        car_handler.receiveSignal(*combine)
        update_server()
    

if __name__ == "__main__":
    main(sys.argv[1:])

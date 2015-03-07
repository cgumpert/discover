import sys
from CarHandlerModule import CarHandler
from Location import Location

def main(argv):
    car_handler = CarHandler()
    
    for time in xrange(0, time_end):
        signal = sig_injector()
        signal += bgk_injector()
        car_handler.receiveSignal(signal)
    

if __name__ == "__main__":
    main(sys.argv[1:])

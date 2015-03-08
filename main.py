import sys, argparse
import httplib, urllib
from CarHandlerModule import CarHandler
from Location import Location
from LocationFinder import LocationFinder
from SignalInjector import SignalInjector
from BackgroundInjector import BackgroundInjector
from Clock import clock
import time
import math

#_______________________________________ 
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
    
#_______________________________________ 
def main(argv):
    # setup argparse
    argument_parser = setupArgParse()
    args = argument_parser.parse_args()

    print vars(args)

    args.func(args)


#_______________________________________ 
def runLive(args):
    car_handler = CarHandler()
    loc_finder = LocationFinder()
    #car_handler.initialise( loc_finder.createRndLocations(300) )
    #car_handler.initialise( loc_finder.loadLocationListFromPickle("share/locationList1000.p") )

    if args.rnd_cars:
        args.rnd_cars = abs(args.rnd_cars)
        car_handler.initialise( loc_finder.createRndLocations(args.rnd_cars) )
    else:
        car_handler.initialise( loc_finder.loadLocationListFromPickle(args.location_file) )

    sig_injector = SignalInjector()
    bgk_injector = BackgroundInjector(threshold=0.4)
    clock.setEnd(args.timesteps)
    for _ in clock:
        print clock.time
        if clock.time == args.timesteps - 1 and args.record_file == "":
            clock.reset()
        
        if clock.time == 10:
            sig_injector.startShower(loc0 = Location(13.735, 51.04),
                                     h0 = 25000,
                                     phi = 0.,
                                     angle = 0.,
                                     sigma = 0.3,
                                     dt = 3e-7)
        if clock.time == 25:
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
        update_server(args.record_file, "")

#_______________________________________ 
def runReplay(args):
   clock.setEnd(args.timesteps)
   for _ in clock:
       print clock.time
       update_server("", args.input_file)
       time.sleep(args.time_per_frame)

#_______________________________________ 
def setupArgParse():
    ## base parser
    base_parser = argparse.ArgumentParser(add_help = False,
                                          formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    base_parser.add_argument('-t', '--timesteps',
                             type = int,
                             default = 100,
                             help = "Number of timesteps")

    ## main parser
    desc = "Discovery !!!"
    main_parser = argparse.ArgumentParser(description = desc)
    subparsers = main_parser.add_subparsers()

    ## sub parser
    # live
    live_parser = subparsers.add_parser('live', parents = [base_parser],
                                        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
                                        help = 'Run simulation live')
    live_parser.set_defaults(func=runLive)
    
    live_parser.add_argument('-r', '--record_file',
                             type = str,
                             default = "",
                             help = "Simulation will be saved in given file name")

    live_parser.add_argument('-l', '--location_file',
                             type = str,
                             default = "share/locationList1000.p",
                             help = "File with car location informations")

    live_parser.add_argument('--rnd_cars',
                             type = int,
                             default = None,
                             help = "Will add given number of cars in random locations. Option will overwrite location file")


    # record
    replay_parser = subparsers.add_parser('replay', parents = [base_parser],
                                          formatter_class = argparse.ArgumentDefaultsHelpFormatter,
                                          help = 'Replay recorded simulation')
    replay_parser.set_defaults(func=runReplay)

    replay_parser.add_argument('-i', '--input_file',
                                type = str,
                                default = "save_events.pickle",
                                help = "Input file with recorded data")

    replay_parser.add_argument('--time_per_frame',
                               type = float,
                               default = 1.0,
                               help = "Time intervall to frame")

    # return parser
    return main_parser


#_______________________________________ 
if __name__ == "__main__":
    main(sys.argv[1:])

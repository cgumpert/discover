################################################################################
# Implementation of CarHandler
################################################################################

# python include(s)

# package include(s)
from CarModule import Car
from Location import Location


################################################################################
class CarHandler(object):
    #_______________________________________ 
    def __init__(self):
        self.__listOfCars = []
        self.__isInit = False
    
    #_______________________________________ 
    def __getitem__(self, idx):
        return self.__listOfCars[idx]
    
    #_______________________________________ 
    def __repr__(self):
        return self.__listOfCars.__repr__()
    
    #_______________________________________ 
    def __str__(self):
        return self.__listOfCars.__repr__()
    
    #_______________________________________ 
    def receiveSignal(self, sigFunc):
        pass
    
    ########################################        
    # Getter
    ######################################## 

    #_______________________________________ 
    def getCarList(self):
        return self.__listOfCars


    ########################################        
    # Initialisation
    ######################################## 
    
    #_______________________________________ 
    def clear(self):
        self.__listOfCars = []
        self.__isInit = False
    
    #_______________________________________ 
    def isInit(self): return self.__isInit
    
    #_______________________________________ 
    def initialise(self, locationList):
        try:
            self.clear()
            for location in locationList:
                self.__listOfCars.append(Car(location))
       
            self.__isInit = True
        
        except:
            print "CarHandler - Error during initialisation"
            self.clear()
            raise

    #_______________________________________ 
    
    
    #_______________________________________ 
    #_______________________________________ 
    






import threading
import sys
import time

class Threaded_Module (threading.Thread):
    def __init__(self,Verbose = True):
        super().__init__()
        self.name = "Empty module"
        self.exitFlag  = 0 #put to one when its time to stop
        self.Verbose = Verbose
    
    #Override me
    def ModuleStop(self): #called when stopping the thread to stop midi output for example 
        print("*mod stopping stuff*")

    def stop(self): #call me to stop this thread
        self.exitFlag = 1
        print(" - "+self.name+" stopping")
        self.ModuleStop()

    
    #Override me
    def run(self):
        print(" - module "+ self.name + " running")

        while(self.exitFlag == 0):
            if self.Verbose:
                print("I ," + self.name +", am running")
            time.sleep(2)
        
        





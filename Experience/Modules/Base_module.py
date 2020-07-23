import threading
import sys
import time

class Threaded_Module (threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = "Empty module"
        self.exitingFlag  = 0 #put to one when its time to stop
    
    def onStop(self): #called when stopping the thread to stop midi output for example 
        print("onstop")

    def stopThread(self): #call me to stop this thread
        self.exitingFlag = 1

    def run(self):
        print(" - module "+ self.name + " running")

        while(self.exitingFlag == 0):
            print("I ," + self.name +" am running")
            time.sleep(2)
        print(" - stopping module "+ self.name)
        self.onStop()





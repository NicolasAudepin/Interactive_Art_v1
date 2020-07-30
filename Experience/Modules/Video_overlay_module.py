
import threading
import random
import sys
import time
from .Base_module import Threaded_Module


class VideoOver_Mod (Threaded_Module):
    """A module that reads a video and gives to the experience easy whays to overlay it;
    """
    def __init__(self,video):
        
        Threaded_Module.__init__(self)
        self.name = "Midi out"
        
        print(" - loading video")

       

            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):





    def ModuleStop(self):
        
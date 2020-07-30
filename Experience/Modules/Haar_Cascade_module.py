import time
import numpy as np
import cv2

from os import listdir
from os.path import isfile, join,relpath


from .Base_module import Threaded_Module

import threading

class HaarCasMod(Threaded_Module):
    def __init__(self,cascades_path,cascade_list,Verbose = False):
        Threaded_Module.__init__(self)
        self.name = "Haar Cascade Module"
        self.path = cascades_path
        self.image_input = False
        self.results = []


        print(" - Loading Haar Cascades from files")
        if Verbose:
            for f in  listdir(self.path):
                print (f)

        self.cas_list = []
        for f in cascade_list:

            self.cas_list.append((cv2.CascadeClassifier(join(self.path, f)),f))


    def set_input_image(self,im):
        self.image_input = im


    def run(self):
        while(self.exitFlag ==0):
            if type(self.image_input) != bool  :
                
                gray = cv2.cvtColor(self.image_input, cv2.COLOR_BGR2GRAY)
    
                self.results = []
                for cas,name in self.cas_list:
                
                    self.results.append((cas.detectMultiScale(gray,
                        scaleFactor = 1.1,
                        minNeighbors =20,
                        minSize = (4, 4),
                        maxSize = (400,400)
                        ),name))


                
                
        
    def ModuleStop(self):
        print(" - Stopping Cascades")
        


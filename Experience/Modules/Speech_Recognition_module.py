
import threading
import random
import sys
import time
from .Base_module import Threaded_Module

import speech_recognition as sr

class Speech_Recognition (Threaded_Module):
    """A module that allows to output midi signals to a choosen midi port.
    using the float_to_midi class it send updated midi signals representing the float values
    """
    def __init__(self):
        
        Threaded_Module.__init__(self)
        self.name = "Speech Recognition"
        
        self.text = ""

        print(" - importing speech recognition")
        
        self.r = sr.Recognizer()
        
            
    def run(self):
        print (" - start " + self.name)
        
        with sr.Microphone() as source:
            print(source)
            while(self.exitFlag ==0):
                print("listeniing ? i guess")
                audio = self.r.listen(source)
                print("audio")
                try :
                    self.text = r.recognize_sphinx(audio)
                except : 
                    print("exxe")



    def ModuleStop(self):
        print("")


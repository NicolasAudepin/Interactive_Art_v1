
import threading
import random
import sys
import time
from .Base_module import Threaded_Module


import speech_recognition as sr

class Speech_Recognition (Threaded_Module):
    """A module that listen to the user and create a text buffer from it.
    If Sphinx is used it works offline but the Google algo uses theire server. 
    """
    def __init__(self,device_index=2,Sphinx = True,Google = True,showmic=False,textbuffersize=3000):
        
        Threaded_Module.__init__(self)
        self.name = "Speech Recognition"
        
        self.textbuffersize = textbuffersize

        print(" - setting speech recognition")

        if showmic:
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        self.sphinx = False
        if Sphinx:
            self.sphinx = True
            self.textBuffS = ""
        self.device_index = device_index
        
        self.google = False
        if Google:
            self.google = True
            self.textBuffG = ""


        self.device_index = device_index
        
        self.r = sr.Recognizer()




        
            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag == 0):
            with sr.Microphone(device_index=self.device_index) as source: # the index controls the source of the audio
                self.audio = self.r.listen(source)
            if self.sphinx:
                try:
                    txt =   self.r.recognize_sphinx(self.audio)
                    print("Sphinx: " + txt)
                    self.textBuffS += " "+txt 

                    diff = len(self.textBuffS) - self.textbuffersize
                    if diff>0:
                        self.textBuffG = self.textBuffG[diff:]

                except sr.UnknownValueError:
                    print("Sphinx could not understand audio")
                except sr.RequestError as e:
                    print("Sphinx error; {0}".format(e))

                


            if self.google:
                try:
                    txt = self.r.recognize_google(self.audio)
                    print("Google: " + txt)
                    self.textBuffG += " "+txt

                    diff = len(self.textBuffG) - self.textbuffersize
                    if diff>0:
                        self.textBuffG = self.textBuffG[diff:]
            

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
            


                        


    def ModuleStop(self):
        print("")


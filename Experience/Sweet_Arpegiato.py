from Experience.experience import Experience as exp

#from ..Modules.keras_yolo3 import yolo as yolo


from .Filter_Modules.sounds.Module_SimpleAudio import SoundLoops

import cv2
from PIL import Image, ImageFont, ImageDraw
import tensorflow as tf
import PIL.ImageDraw
import random

from os import listdir
from os.path import isfile, join
import numpy as np
import colorsys
import os
from timeit import default_timer as timer
from .Filter_Modules.Tracking_module import multi_Tracker_Module , Tracker
            


class Sweet_Arpegiato(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Sweet Arpegiato"



            from .Filter_Modules.Midi_output_module import MidiOutMod
            self.midiout= MidiOutMod()

            print(" - loading sounds")
            from .Filter_Modules.sounds.Module_SimpleAudio import SoundLoops
            self.sound_to_track = [ 0 for i in range(7)]

            self.JukBox  = SoundLoops()     
            self.JukBox.start()

            print(" - loading Yolo")  
            from .Filter_Modules.keras_yolo3 import yolo         
            global graph # needed for yolo to read the images stuff to do with multi threading
            graph = tf.get_default_graph()
            self.Y = yolo.YOLO()

            print(" - setting Tracking module")
            from .Filter_Modules.Tracking_module import multi_Tracker_Module , Tracker
            self.multi_Tracker = multi_Tracker_Module(dim=4,labeled = True)
            self.multi_Tracker.start()


            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):


        imageasarray = Image.fromarray(image)


        #use yolo to get new coordonates and give them to analize to the multi tracker
        with graph.as_default():
            res = self.Y.detect_image(imageasarray)
         #print(res)
        self.multi_Tracker.set_new_coordonates(res)



        # get the trackers to draw 
        trackers = self.multi_Tracker.tracker_list
        
        
        
        #remove lost trackers
        for i in range(len(self.sound_to_track)):
            obj = self.sound_to_track[i]
            if type(obj) == Tracker:
                if obj not in trackers:
                    self.sound_to_track[i]=0

        #add new trackers to the sound list
        for t in trackers:
            if t  not in self.sound_to_track and 0 in self.sound_to_track:
                i = self.sound_to_track.index(0)
                self.sound_to_track[i] = t

        soundlist = []

        for i in range(len(self.sound_to_track)):
            obj = self.sound_to_track[i]
            if type(obj) == Tracker:

                soundlist.append(i)
        self.JukBox.nextloops = soundlist


        #draw all trackers 
        for tracker in trackers:
             
            if False:

                #draw the prediction
                x,y,a,b = tracker.current_position_estimation
                x= int(x)
                y = int(y)
                a= int(a)
                b = int(b)
                color = tracker.pred_color()
                #print( (x, y), (a, b), color, 2)
                cv2.rectangle(image, (x, y), (a, b), color, 2)

            #draw the last known position
            x,y,a,b = tracker.last_known_position
            color = tracker.color()
            cv2.rectangle(image, (x, y), (a, b), color, 4)
            text = tracker.label +" "+str(tracker.certainty)
            cv2.putText(image,tracker.label, 
                (x,y), 
                self.font, 
                self.fontScale,
                color,
                self.lineType)


        out = image
        return out
    
    def stop(self):
        self.JukBox.exitFlag=1
        self.multi_Tracker.exitFlag = 1
        self.exitFlag = 1
        print(" - Shuting Down  Thread"+ self.name)



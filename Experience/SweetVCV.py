from Experience.experience import Experience as exp

#from ..Modules.keras_yolo3 import yolo as yolo



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
            


class Sweet_VCV(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Sweet VCV"

            
            print(" - loading Yolo")  
            from .Filter_Modules.keras_yolo3 import yolo         
            global graph # needed for yolo to read the images stuff to do with multi threading
            graph = tf.get_default_graph()
            self.Y = yolo.YOLO()

            print(" - setting Tracking module")
            from .Filter_Modules.Tracking_module import multi_Tracker_Module , Tracker
            self.multi_Tracker = multi_Tracker_Module(dim=8,labeled = True)
            self.multi_Tracker.start()
            #must be after the yolo import for some reason
            

            print(" - loading Mido module")
            from .Filter_Modules.Midi_output_module import MidiOutMod, float_to_midi
            
            self.midiout= MidiOutMod('midoVCV 2')

            #tracks the number of objects on channel 1
            self.nb_objectstomidi = float_to_midi('nb_objects',[0,8],10,1)
            self.midiout.signals.append(self.nb_objectstomidi)
            
            #track the size of objects on channel 2
            self.sizetomidi = float_to_midi('size',[0,100000],10,2)
            self.midiout.signals.append(self.sizetomidi)
            
            self.midiout.start()

            


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

        self.nb_objectstomidi.set_val(len(res))

        
        self.multi_Tracker.set_new_coordonates(res)

        # get the latest trackers from the tracking module 
        trackers = self.multi_Tracker.tracker_list
        

        #TODO do midi stuff with them
        
        
        #draw all trackers onto the output image
        for tracker in trackers:
             
            
            #draw the prediction
            """
            x,y,a,b = tracker.current_position_estimation
            x= int(x)
            y = int(y)
            a= int(a)
            b = int(b)
            color = tracker.pred_color()           
            #print( (x, y), (a, b), color, 2)
            cv2.rectangle(image, (x, y), (a, b), color, 2)
            """
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
        areas = [area(tracker.last_known_position) for tracker in trackers]
        print(areas)

        self.sizetomidi.set_val(int(max(areas,default=0)))

        
        out = image
        return out
    
    def stop(self):
        print(" - Shuting Down  Experience "+ self.name)
        self.midiout.exitFlag=1
        self.multi_Tracker.exitFlag = 1
        self.exitFlag = 1
        

def area4(a,b,x,y):
    return abs(a-b)*abs(x-y)

def area(list):
    return area4(list[0],list[1],list[2],list[3])

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


class Cloud(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Cloud VCV"

            
            print(" - loading Yolo")  
            from .Modules.keras_yolo3 import yolo         
            global graph # needed for yolo to read the images stuff to do with multi threading
            graph = tf.get_default_graph()
            self.Y = yolo.YOLO()


            print(" - loading Mido module")
            from .Modules.Midi_output_module import MidiOutMod, float_to_midi           
            self.midiout= MidiOutMod('midoVCV 2')
            
            #tracks the number of objects on channel 1
            self.touchingmid = float_to_midi('touching',[0,1],10,3)
            self.midiout.signals.append(self.touchingmid)

            self.moduleslist.append(self.midiout)
            
            self.midiout.start()

            
            
            print("- import vid")
            from.Modules.Video_Loop_module import Video_Loop_Mod
            self.color = Video_Loop_Mod("Experience\\Modules\\Videos\\cloud_color.mp4",input_shape)
            self.moduleslist.append(self.color)
            self.color.start()
            self.error = Video_Loop_Mod("Experience\\Modules\\Videos\\cloud_error.mp4",input_shape)
            self.moduleslist.append(self.error)
            self.error.start()
            

            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2
            
    
    def Are_touching(self,r1,r2):
        (label1, l1,t1,r1,b1) = r1
        (label2, l2,t2,r2,b2) = r2

        lr = (l1 > l2 and l1<r2) or (r1 > l2 and r1<r2) 
        tb = (t1 > t2 and l1<b2) or (r1 > t2 and r1<b2)

        return lr and tb 


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):

        #use yolo to get new coordonates and give them to analize to the multi tracker
        imageasarray = Image.fromarray(image)
        with graph.as_default():
            res = self.Y.detect_image(imageasarray)
         #print(res)

        res = [(label, l,t,r,b) for (label, l,t,r,b) in res if label == 'person']

        touching = 0
        for i in range(len(res)):
            for j in range(len(res)):
                if i != j and self.Are_touching(res[i],res[j]): 
                    touching = 1

        self.touchingmid.set_val(touching)


        out = self.color.output_image * (1-touching) + self.error.output_image * touching

        # put the people among the fishes
        for (label, l,t,r,b) in res:
            out [t:b,l:r] = image[t:b,l:r]
        



        return out
    




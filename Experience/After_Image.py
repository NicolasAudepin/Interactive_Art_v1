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


class After_Image(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Sweet VCV"

            
            print(" - loading Yolo")  
            from .Modules.keras_yolo3 import yolo         
            global graph # needed for yolo to read the images stuff to do with multi threading
            graph = tf.get_default_graph()
            self.Y = yolo.YOLO()


            print(" - loading Mido module")
            from .Modules.Midi_output_module import MidiOutMod, float_to_midi           
            self.midiout= MidiOutMod('midoVCV 2')
            
            #tracks the number of objects on channel 1
            self.nb_objectstomidi = float_to_midi('nb_objects',[0,5],10,1)
            self.midiout.signals.append(self.nb_objectstomidi)

            self.moduleslist.append(self.midiout)
            
            #self.midiout.start()

            


            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2
            
            self.out = np.zeros(input_shape,dtype=np.uint8)
            
    

    #this called in the while loop and take as input an image
    def Treat_Image(self,image):

        #use yolo to get new coordonates and give them to analize to the multi tracker
        imageasarray = Image.fromarray(image)
        with graph.as_default():
            res = self.Y.detect_image(imageasarray)
         #print(res)

        res = [(label, l,t,r,b) for (label, l,t,r,b) in res if label == 'person']

        #self.nb_objectstomidi.set_val(len(res))


        


        # put the people among the fishes
        for (label, l,t,r,b) in res:
            self.out [t:b,l:r] = image[t:b,l:r]
        



        return self.out
    


from Experience.experience import Experience as exp


#basic stuff
import numpy as np
import datetime
import threading
import time

#image stuff
import cv2
from PIL import Image, ImageFont, ImageDraw

#my modules




class testExp(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Basic experience"
            
            print(" - importing Base module")
            from .Modules.Base_module import Threaded_Module as TM
            self.module = TM()
            self.moduleslist.append(self.module)
            self.module.start()

            print(" - loading Mido module")
            from .Modules.Midi_output_module import MidiOutMod, float_to_midi           
            self.midiout= MidiOutMod('midoVCV 2')
            
            #tracks the number of objects on channel 1
            self.nb_objectstomidi = float_to_midi('nb_objects',[0,8],10,1)
            self.midiout.signals.append(self.nb_objectstomidi)

            self.moduleslist.append(self.midiout)
            self.midiout.start()

            

            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):

        imageasarray = Image.fromarray(image)
        out = image % 64

        self.nb_objectstomidi.set_val(4)

        return out
    


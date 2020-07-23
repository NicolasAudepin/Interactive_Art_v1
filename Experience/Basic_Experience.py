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
from .Modules.Base_module import Threaded_Module as TM



class Example_experience(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Basic experience"
            
            print(" - importing Base module")
            self.module = TM()
            self.module.start()

            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):


        imageasarray = Image.fromarray(image)

        out = image % 64


        return out
    
    def stop(self):
        self.exitFlag = 1
        print(" - Shuting Down Modules")
        self.module.stopThread()



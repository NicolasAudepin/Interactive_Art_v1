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
from .Modules.Video_Loop_module import Video_Loop_Mod



class testExp(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Basic experience"
            
            print(" - importing Base module")
            from .Modules.Base_module import Threaded_Module as TM
            self.module = TM()
            self.moduleslist.append(self.module)
            self.module.start()


            print("- import vid")
            self.vid = Video_Loop_Mod("Experience\\Modules\\Videos\\cubesloop.mp4",input_shape)
            self.moduleslist.append(self.vid)
            self.vid.start()
            

            

            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):

        #print("treat image input",image.shape)

        imageasarray = Image.fromarray(image)
        out = image % 64 
        
        out = out + self.vid.output_image


        return out
    


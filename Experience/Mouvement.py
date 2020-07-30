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


class Mouvement_experience(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Basic experience"
            print(input_shape)
            self.white_screen = np.ones(input_shape)*100 
            


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):
        print("dddd")
        print(self.white_screen.size)
        image = np.minimum(image ,self.white_screen)
        print(type(image), image.size )

        out = image

        return out
    


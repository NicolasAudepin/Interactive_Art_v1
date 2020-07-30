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
from .Modules.Haar_Cascade_module import HaarCasMod


class Joconde(exp):
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Joconde"
            
            print(" - importing Haar module")
            cascadelist = ['haarcascade_smile.xml','haarcascade_eye.xml']
            self.haar = HaarCasMod('Experience\\Modules\\opencvHaarCascade',cascadelist)
            self.moduleslist.append(self.haar)
            self.haar.start()

            print(" - importing images")
            self.smile = cv2.imread("Experience\\Modules\\Images\\Joconde\\Mona_Lisa_detail_mouth.jpg")
            self.eye = cv2.imread("Experience\\Modules\\Images\\Joconde\\Mona_Lisa_detail_eye.jpg")


 

    #this called in the while loop and take as input an image
    def Treat_Image(self,image):

        self.haar.set_input_image(image)

        res = self.haar.results
        for haarres in res:

            if haarres[1] == 'haarcascade_smile.xml':
                im = self.smile
            elif haarres[1] == 'haarcascade_eye.xml':
                im = self.eye

            for (x,y,w,h) in haarres[0]:
                im_resized = cv2.resize(im,(w,h))
                image[y:y+h,x:x+w] = im_resized



        return image
    


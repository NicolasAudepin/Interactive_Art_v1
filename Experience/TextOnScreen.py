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


                                        

class TextOnScreen(exp):
        """
        Show what it hears
        """

        def __init__(self, threadID, input_shape):        
                exp.__init__(self, threadID, input_shape)
                self.name = "Text On Screen"

                print(" - Speech recognition stuff")
                from .Modules.Speech_Recognition_module import Speech_Recognition as SR
                self.speechmod = SR(device_index=2,Google = True,showmic=False)
                self.moduleslist.append(self.speechmod)
                self.speechmod.start()


                print(" - text stuff")
                self.text = ""
                print(" - visual stuff")
                #cv2 put text stuff
                self.font = ImageFont.truetype('Fonts\\typewriter\\TYPEWR__.TTF', 30)
                print(self.font)
                self.fontScale = 1
                self.lineType = 2
                self.textcolor = (0,0,0)


        #this called in the while loop and take as input an image
        def Treat_Image(self,image):


                imageasarray = Image.fromarray(image)
                self.text = self.speechmod.textBuff
                draw = ImageDraw.Draw(imageasarray)
                draw.text((10,10), self.text, font=self.font, fill=(0,0,0))


                out = np.array(imageasarray)  

                return out



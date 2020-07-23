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
    def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Text On Screen"

            print(" - Speech recognition stuff")
            from .Modules.Speech_Recognition_module import Speech_Recognition as SR
            self.speechmod = SR()
            self.moduleslist.append(self.speechmod)
            self.speechmod.start()

        
            print(" - text stuff")
            self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquet volutpat nibh, sed tempus arcu.\n Suspendisse sagittis justo nec turpis maximus cursus ac quis tellus. Mauris tincidunt risus quis nunc convallis, sed vehicula nisl consectetur. Nulla laoreet mauris leo, non varius odio aliquet in. Nunc viverra enim et felis ultrices ornare. Donec sollicitudin, augue ac tempus consequat, velit leo tincidunt dui, nec tristique justo arcu pharetra arcu. Cras finibus, nunc gravida aliquam tempor, massa tellus hendrerit velit, a bibendum purus urna quis urna. Praesent efficitur ante quis molestie vulputate. Nunc vitae vehicula felis, ac pretium purus. Quisque id mattis purus, sed facilisis est. Fusce rhoncus eros ullamcorper nulla sollicitudin molestie."

            print(" - visual stuff")
            #cv2 put text stuff
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            self.fontScale = 1
            self.lineType = 2
            self.textcolor = (0,0,0)


    #this called in the while loop and take as input an image
    def Treat_Image(self,image):
        fnt = ImageFont.truetype('arial.ttf', 30)

        imageasarray = Image.fromarray(image)

        draw = ImageDraw.Draw(imageasarray)
        draw.text((10,10), self.text, font=fnt, fill=(0,0,0))
        

        out = np.array(imageasarray)  
       
        return out
    

"""
from PIL import Image, ImageDraw, ImageFont
import os
 
def text_on_img(filename='01.png', text="Hello", size=12):
	"Draw a text on an Image, saves it, show it"
	fnt = ImageFont.truetype('arial.ttf', size)
	# create image
	image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = "red")
	draw = ImageDraw.Draw(image)
	# draw text
	draw.text((10,10), text, font=fnt, fill=(255,255,0))
	# save file
	image.save(filename)
	# show file
	os.system(filename)
 
 
text_on_img(text="Text to write on img", size=300)
"""
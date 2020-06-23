from Experience.experience import Experience as exp

#from ..Modules.keras_yolo3 import yolo as yolo
from .Filter_Modules.keras_yolo3 import yolo
import cv2

from PIL import Image as PIm
import PIL.ImageDraw
import random

from os import listdir
from os.path import isfile, join
import numpy as np
import colorsys
import os
from timeit import default_timer as timer


class Sweet_Dawn(exp):
        def __init__(self, threadID, input_shape):        
            exp.__init__(self, threadID, input_shape)
            self.name = "Sweet Dawn"

            print(" - loading Yolo")
            self.Y = yolo.YOLO()

            print(" - loading sound")
            import simpleaudio as sa
            #D:\Documents\GitHub\Interactive_Art_v1\Experience\Filter_Modules\sounds\sweet_arpegiato
            sample_folder = "D:\\Documents\\GitHub\\Interactive_Art_v1\\Experience\\Filter_Modules\\sounds\\sweet_arpegiato" 
            onlyfiles = [f for f in listdir(sample_folder) if isfile(join(sample_folder, f))]
            
            self.sound_list = []
            
            i = 0
            for f in onlyfiles:
                print(str(i), f)
                r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                name = str(i)
                i+=1
                self.sound_list.append((sa.WaveObject.from_wave_file(join(sample_folder, f)),(r,g,b),name))
            self.alone = sa.WaveObject.from_wave_file("D:\\Documents\\GitHub\\Interactive_Art_v1\\Experience\\Filter_Modules\\sounds\\Ya personne.wav") 
            self.playing_sounds = []
            self.silent_sounds = [i for i in range(len(self.sound_list))]

        def Treat_Image(self,image):
            self.Y = yolo.YOLO()

            mask = np.zeros(self.input_shape,np.uint8)        
            
            print(image)
            print(image.shape)
            
            cul = PIm.fromarray(image)
            

            res = self.Y.detect_image(cul)
            nb_people = 0

            for (label, l,t,r,b) in res:
                
                if (label == 'person'and len(self.silent_sounds) > 0 ):

                    rdm = random.randint(0,len(self.silent_sounds)-1)

                    self.playing_sounds.append(silent_sounds[rdm])
                    silent_sounds.remove(silent_sounds[rdm])

                    print(l,t,r,b)
                    mask[t:b,l:r]= np.ones((b-t,r-l,3))*1

 
            output = image * mask 
                
                    
                    

            return output
    
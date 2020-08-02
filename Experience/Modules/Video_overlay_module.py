
import threading
import random
import sys
import time
from .Base_module import Threaded_Module

import numpy as np
import cv2


class VideoOver_Mod (Threaded_Module):
    """A module that reads a video and gives to the experience easy whays to overlay it;
    """
    def __init__(self,video_file,input_shape):
        
        Threaded_Module.__init__(self)
        self.name = "Video Overlay "
        self.output_image = []
        self.output_mask = []
        self.video_shape = input_shape
        print(" - loading video")

        self.path = video_file

        self.cap = cv2.VideoCapture(self.path)

        
        ret, frame = self.cap.read()
        self.output_image = cv2.resize(frame,(self.video_shape[1],self.video_shape[0]))

            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag == 0):
            # Capture frame-by-frame

            ret, frame = self.cap.read()

            if ret:
                self.output_image = cv2.resize(frame,(self.video_shape[1],self.video_shape[0]))
            
            else:
                print("another one")
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
   
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break




    def ModuleStop(self):
        self.cap.release()                



"""


cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""
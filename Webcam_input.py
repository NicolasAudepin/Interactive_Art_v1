import numpy as np
import cv2
import datetime
import threading
import time

cap = cv2.VideoCapture(0)
input_shape = (480, 640, 3)   #(256,256,3)


class Webcam_input(threading.Thread):
    def __init__(self):

        self.webcam_shape = 0
        self.image_output_shape = 0
        self.current_frame = 0

    def run(self):
        
print("*** GENERAL IMPORTS ***")
import numpy as np
import cv2
import datetime
import threading
import time

print("*** SETTING VIDEO ***")
cap = cv2.VideoCapture(0)
input_shape = (256,256,3)

input_file = 'D:\\Documents\\Blender\\RENDERS\\Sunset\\0001-0250v1shsfhsfh.avi'
cap = cv2.VideoCapture(input_file)

print("*** CHOOSE YOUR EXPERIENCE ***")



print("*** INITIALISE EXPERIENCE ***")
#from Experience.experience import Experience as exp
#experience = exp(1,  input_shape = input_shape)
from  Experience.Sweet_Dawn import Sweet_Dawn
from Experience.Sweet_Arpegiato import Sweet_Arpegiato

experience = Sweet_Arpegiato(1,input_shape)

print(" - Experience : "+ experience.name)
experience.start()


print("*** STARTING ***")
print("press q to exit")
exitFlag = 0
while(exitFlag == 0):
    
    ret, frame = cap.read()
    experience.setInputImage(frame)
    output_im = experience.getOutputImage()

    cv2.imshow('frame',cv2.resize(output_im,(600,600)))

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # press q to exit
        experience.stop()
        exitFlag = 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


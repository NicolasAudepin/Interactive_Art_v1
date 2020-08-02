print("*** GENERAL IMPORTS ***")
import numpy as np
import cv2
import datetime
import threading
import time

print("*** SETTING WEBCAM ***")
cap = cv2.VideoCapture(0)
input_shape = (480, 640, 3)   #(256,256,3)

print("*** CHOOSE YOUR EXPERIENCE ***")

print(" -1 Example Experience ")
print(" 0 Default experience ")
print(" 1 Sweet Dawn (crashes)")
print(" 2 Sweet Arpegiato ")
print(" 3 Sweet VCV ")
print(" 4 TextOnScreen")
print(" 5 Mouvement (crashes)")
print(" 6 Joconde")
print("\nChoose an experience")
nb = input()

print("*** INITIALISE EXPERIENCE ",nb ," ***")

if nb =="-1":
    from Experience.Basic_Experience import Example_experience
    experience = Example_experience(1,input_shape)
elif nb =="0":
    from Experience.experience import Experience as exp
    experience = exp(1,  input_shape = input_shape)
elif nb =="1":
    from  Experience.Sweet_Dawn import Sweet_Dawn
    experience = Sweet_Dawn(1,  input_shape = input_shape)
elif nb =="2":
    from Experience.Sweet_Arpegiato import Sweet_Arpegiato
    experience = Sweet_Arpegiato(1,input_shape)
elif nb =="3":
    from Experience.SweetVCV import Sweet_VCV
    experience = Sweet_VCV(1,input_shape)

elif nb =="4":
    from Experience.TextOnScreen import TextOnScreen
    experience = TextOnScreen(1,input_shape)
elif nb =="5":
    from Experience.Mouvement import Mouvement_experience
    experience = Mouvement_experience(1,input_shape)
elif nb =="6":
    from Experience.Joconde import Joconde
    experience = Joconde(1,input_shape)
else:
    from Experience.TestExp import testExp as exp
    experience = exp(1,  input_shape = input_shape)
#from Experience.experience import Experience as exp
#experience = exp(1,  input_shape = input_shape)

#from  Experience.Sweet_Dawn import Sweet_Dawn





print(" - Experience : "+ experience.name)
experience.start()


print("*** STARTING ***")
print("press q to exit")
exitFlag = 0
while(exitFlag == 0):

    #import pathlib
    #print(pathlib.Path().absolute())
    
    ret, frame = cap.read()
    #print("cap read",frame.shape)
    experience.setInputImage(frame)
    output_im = experience.getOutputImage()

    #all the visual stuff independant from the experience like displayed resolution should be handeled here 

    cv2.imshow('frame',cv2.resize(output_im,(1830,1200)))#roughly projector size

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # press q to exit
        experience.stop()
        exitFlag = 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


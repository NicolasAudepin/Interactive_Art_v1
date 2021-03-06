

import threading
import time
import numpy as np

"""
The default experience. 
the main thread continuously updates its input image and gets its output image.
In theory, all this class and the classes inheriting from it should have to do is using the Treat_Image function
to update the ouput image.   


"""
class Experience (threading.Thread):
    #reuse this
    def __init__(self, threadID, input_shape):
        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = "default experience"
        self.input_shape = input_shape
        self.input_im = np.zeros(input_shape,np.uint8)
        self.output_im = np.zeros(input_shape,np.uint8)
        self.exitFlag = 0 
        self.moduleslist = []

    def setInputImage(self,image):
        self.input_im = image


    #Override this 
    def Treat_Image(self,image):

        output = image % 128

        return output
    
    def stop(self):#called by the main and should theorically not be overrident 
        self.exitFlag = 1
        time.sleep(0.4)#waiting for the while loop to stop for cleaner prints
        print(" - Shuting Down Modules")
        for mod in self.moduleslist:
            mod.stop()


    def run(self):#called by the main
        print (" - Starting " + self.name)
        while(self.exitFlag ==0):
            input_im = self.input_im
            self.output_im = self.Treat_Image(input_im)

        #when stopped    
        print (" - Exiting " + self.name)

    def getOutputImage(self):
        return self.output_im




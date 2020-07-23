
from os import listdir
import threading
import random
from os.path import isfile, join
from ..Base_module import Threaded_Module

class SoundLoops (Threaded_Module):
    def __init__(self,sample_folder,beat_file):
        """A module that allows to read sound loops from a folder.
        All the loops are read at once from a selection of them made in self.nextloops  
        """
        Threaded_Module.__init__(self)

        self.name = "sound loops"
 
        self.nextloops = []

        print(" - loading sound")
        import simpleaudio as sa
        onlyfiles = [f for f in listdir(sample_folder) if isfile(join(sample_folder, f))]
        
        self.sound_list = []
        i = 0 
        for f in onlyfiles:
            print(str(i), f)
            r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
            name = str(i)
            i+=1
            self.sound_list.append((sa.WaveObject.from_wave_file(join(sample_folder, f)),(r,g,b),name))
        self.beat = sa.WaveObject.from_wave_file(beat_file) 
        
    def SetNextLoops(self,looplist):
        self.nextloops = looplist
            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):
            play_beat = self.beat.play()

            for  l in self.nextloops:
                if (l < len(self.sound_list)):
                    self.sound_list[l][0].play()       
            play_beat.wait_done()        
        
    def ModuleStop(self):
        print("waiting for the loops to end")

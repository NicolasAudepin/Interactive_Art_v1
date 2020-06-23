
from os import listdir
import threading
import random
from os.path import isfile, join


class SoundLoops (threading.Thread):
    def __init__(self):
        
        threading.Thread.__init__(self)

        self.name = "sound loops"
        self.exitFlag =0
        self.nextloops = []

        print(" - loading sound")
        import simpleaudio as sa
        sample_folder = "D:\\Documents\\GitHub\\Interactive_Art\\sounds" 
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
        self.beat = sa.WaveObject.from_wave_file("D:\\Documents\\GitHub\\Interactive_Art_v1\\Experience\\Filter_Modules\\sounds\\swet_beat\\Sweet Arpeges 9-SessionDry Kit.wav") 
        
    def SetNextLoops(self,looplist):
        self.nextloops = looplist
            
    def run(self):
        print (" - Loop go " + self.name)
        while(self.exitFlag ==0):
            play_beat = self.beat.play()

            for  l in self.nextloops:
                if (l < len(self.sound_list)):
                    self.sound_list[l][0].play()       
            play_beat.wait_done()        
        print (" - Loop Thread stop " + self.name)

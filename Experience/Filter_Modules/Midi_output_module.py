
import threading
import random

class MidiOut (threading.Thread):
    def __init__(self):
        
        threading.Thread.__init__(self)

        self.name = "Midi out"
        self.exitFlag =0

        print(" - loading mido")

        import mido

        print(" - loading mido")

        port = mido.open_output('midoMod')



            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):
            break
               
        print (" - Loop Thread stop " + self.name)

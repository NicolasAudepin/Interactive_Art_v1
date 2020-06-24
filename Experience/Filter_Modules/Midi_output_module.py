
import threading
import random

class MidiOutMod (threading.Thread):
    def __init__(self):
        
        threading.Thread.__init__(self)

        self.name = "Midi out"
        self.exitFlag =0

        print(" - loading mido")

        import mido

        print(" - setting mido port")

        print(mido.get_output_names())

        port = mido.open_output() 

        print(port.name)



            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):
            break
               
        print (" - Loop Thread stop " + self.name)

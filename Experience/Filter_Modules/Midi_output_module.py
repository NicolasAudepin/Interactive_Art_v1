
import threading
import random
import sys
import time

import mido
from mido import Message 

class MidiOutMod (threading.Thread):
    def __init__(self,midi_port):


        self.signals = []
        
        threading.Thread.__init__(self)

        self.name = "Midi out"
        self.exitFlag =0

        print(" - loading mido")



        print(" - setting mido port")

        print(mido.get_output_names())

        self.port = mido.open_output(midi_port) 

        print(self.port.name)





            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):


            for ftm in self.signals:

                on = Message('note_on', channel = ftm.channel, note=ftm.note,velocity = ftm.midivalue)
                print(on)
                self.port.send(on)

               
        print (" - stop Module" + self.name)
        for ftm in self.signals:
            off = Message('note_off',note=ftm.note)
            print(off)



class float_to_midi():

    def __init__(self, name = "value", value_range = [0,1], note = 1,channel= 1):
        self.name = name
        self.min = value_range[0]
        self.max = value_range[1]
        self.midivalue = self.min
        self.note = note
        self.channel = channel
        



    def set_val(self, floatval):
        vall = min(floatval,self.max) 
        vall = max(vall,self.min) 

        vall = vall - self.min

        self.midivalue =int(vall * 127 / (self.max - self.min))

    

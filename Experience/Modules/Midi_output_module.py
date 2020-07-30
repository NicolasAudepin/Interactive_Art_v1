
import threading
import random
import sys
import time
from .Base_module import Threaded_Module

import mido
from mido import Message 


class MidiOutMod (Threaded_Module):
    """A module that allows to output midi signals to a choosen midi port.
    using the float_to_midi class it send updated midi signals representing the float values
    """
    def __init__(self,midi_port):
        
        Threaded_Module.__init__(self)
        self.name = "Midi out"
        
        print(" - loading mido")
        print(" - setting mido port")
        
        print(mido.get_output_names())
        self.port = mido.open_output(midi_port) 
        print(self.port.name)
        self.signals = []

            
    def run(self):
        print (" - start " + self.name)
        while(self.exitFlag ==0):


            for ftm in self.signals:

                on = Message('note_on', channel = ftm.channel, note=ftm.note,velocity = ftm.midivalue)
                print(on)
                self.port.send(on)


    def ModuleStop(self):
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

        self.midivalue =int(min(1+(vall * 127 / (self.max - self.min)),127))

    

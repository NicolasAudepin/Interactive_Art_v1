import time
import numpy as np
import random
import colorsys
from .Base_module import Threaded_Module

import threading

class multi_Tracker_Module(Threaded_Module):
    def __init__(self, dim,labeled = False,forgeting_speed = 20):
        Threaded_Module.__init__(self)
        self.name = "Tracking Module"

        self.data_waiting = False
        self.last_given_coordonate = []
        self.last_given_time = time.time()
        
        self.labeled = labeled
        self.max_tracker = 8

        self.matching_treshold = 0.001 #matching score needed to match a tracker and some coordiantes
        self.forgeting_speed = self.matching_treshold * forgeting_speed # certanty lost every frame 
        self.forgeting_treshold = 0.4 #below this certainty the tracker is considered lost and is removed


        self.tracker_list = []

    #set new coordinate to be match later
    def set_new_coordonates(self, new_co): 
        self.last_given_time = time.time()
        if self.labeled:
            self.last_given_coordonate = []
            for co in new_co:
                self.last_given_coordonate.append((co[0],np.array(co[1:])))
                
        else:
            self.last_given_coordonate = []
            for co in new_co:
                self.last_given_coordonate.append((None,np.array(co)))
        
        self.data_waiting = True
        
    def score(self,pair1,pair2,labeled =True):

        score = 0
        if labeled:
            l1 ,v1 = pair1
            l2,v2 = pair2
            if l1 == l2:
                dist = np.linalg.norm(v1 - v2)
                score = 1/max(0.00000001,dist)
        else:
            dist = abs(pair1 - pair2)
            score = 1/max(0.00000001,dist)
        return score
                 
    def sortkey(self,x):
        return[x[0]]


    def run(self):
        while(self.exitFlag ==0):
            if(self.data_waiting):
                self.data_waiting = False


                #all certainty lower a bit and the ones too low disapear
                for track in self.tracker_list:
                    track.certainty = track.certainty - self.forgeting_speed 

                    if track.certainty <  self.forgeting_treshold:
                        self.tracker_list.remove(track)


                #prepare assignement between trackers and coordonates 
                unassigned_co = []
                unassigned_tr = []
                for co in self.last_given_coordonate:
                    unassigned_co.append(True)
                for track in self.tracker_list:
                    unassigned_tr.append(True)


                #create all the pairs score
                score_to_pair = []               
                for i in range(len(self.tracker_list)):
                    track = self.tracker_list[i]
                    if self.labeled:
                        pos = [track.label,track.estimate_position_at(self.last_given_time)]
                    else:
                        pos = track.estimate_position_at(self.last_given_time)
                    for j in range(len(self.last_given_coordonate)):
                        co = self.last_given_coordonate[j]

                        score = self.score(co,pos)
                        score_to_pair.append([score,j,i])
                
                #gives the coordonates to the closest tracker
                score_to_pair.sort(key = self.sortkey)
                #print(score_to_pair)
                for pair in score_to_pair:
                    score,cn,tn = pair
                    if unassigned_co[cn] and unassigned_tr[tn] and score > self.matching_treshold:
                        unassigned_co[cn] = False
                        unassigned_tr[tn] = False
                        track = self.tracker_list[tn]
                        co = self.last_given_coordonate[cn]

                        new_certainty = min(track.certainty + score ,1) 

                        track.update_coordonates(co[1],self.last_given_time,new_certainty)

                
                #create new trackers for coordonates without trackers
                for nc in range(len(self.last_given_coordonate)):
                    co = self.last_given_coordonate[nc]
                    if unassigned_co[nc]:
                        if len(self.tracker_list)<self.max_tracker:
                            track = Tracker(self.last_given_coordonate[nc][1],
                                        self.last_given_time,
                                        self.last_given_coordonate[nc][0])
                            self.tracker_list.append(track)

                
        
    def ModuleStop(self):
        print("Shuting Down Trackers")
        



class Tracker():
    def __init__(self,dim):
        self.label = None

        self.last_known_position = np.array([0 for i in range(dim)])
        self.last_known_speed = np.array([0 for i in range(dim)])
        self.last_known_acceleration = np.array([0 for i in range(dim)])
        self.last_time_seen = time.time()
       
        self.current_speed_estimation = np.array([0 for i in range(dim)])
        self.current_position_estimation = np.array([0 for i in range(dim)])
        
        self.certainty = 0.5

        self.id = random.random()


    def __init__(self,original_pos,t,label):
        dim = len(original_pos)
        self.label = label
        self.last_known_position = np.array(original_pos)
        self.last_known_speed = np.array([0 for i in range(dim)])
        self.last_known_acceleration = np.array([0 for i in range(dim)])
        self.last_time_seen = t

        self.current_speed_estimation = [0 for i in range(dim)]
        self.current_position_estimation = np.array(original_pos)

        self.certainty = 0.5
        self.id = random.random()

    def color(self):
        R,G,B = colorsys.hsv_to_rgb(self.id,1,self.certainty)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return (R,G,B) 

    def pred_color(self):
        R,G,B = colorsys.hsv_to_rgb(self.id,0.5,self.certainty)
        R = int(R*255)
        G = int(G*255)
        B = int(B*255)
        return (R,G,B) 

    def estimate_position_at(self,t):       
        dt = t - self.last_time_seen     
        pos_estimate = self.last_known_position + self.last_known_speed * dt + self.last_known_acceleration * dt * dt * 0.5 
        self.current_position_estimation =  pos_estimate
        return pos_estimate
    


    def update_coordonates(self,new_position, new_time, new_certainty):
        dt = new_time - self.last_time_seen
        new_v = (new_position - self.last_known_position) / dt
        new_a = (new_v - self.last_known_speed) / dt

        self.last_known_acceleration = new_a
        self.last_known_speed = new_v
        self.last_known_position = new_position
        self.last_time_seen = new_time
        self.certainty = new_certainty

    
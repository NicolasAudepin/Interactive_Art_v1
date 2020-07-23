import time
import numpy as np

import threading

class multi_Tracker_Module(threading.Thread):
    def __init__(self, dim,labeled = False):
        threading.Thread.__init__(self)
        self.labeled = labeled
        self.max_tracker = 8
        self.matching_treshold = 20
        self.forgeting_treshold = 0.1
        self.current_coordonates = []
        self.tracker_list = []

    def score(elem):
        return elem[0]


    def match_trackers(self):

        matching_time = time.time()

        matches=[]
        for i in range(len(self.tracker_list)):
            track = self.tracker_list[i]
            t_scores = track.get_scores(self.current_coordonates)
            for j in range(len( t_scores)):
                if t_scores[j] < self.treshold:
                    matches.append[t_scores[j],i,j]
        matches.sort(key = score)

        free_trackers = [True for i in range(len(self.tracker_list))]
        free_points = [True for i in range(len(self.current_coordonates))]

        for match in matches:
            if free_trackers[match[1]] and free_points[match[2]]:
                free_trackers[match[1]] = False
                free_points[match[2]] = False
                updated_tracker = self.tracker_list[match[1]]
                choosen_coordonates = self.current_coordonates[match[2]]
                updated_tracker.update_coordonates(new_position = choosen_coordonates, new_time = matching_time, new_certainty = 0.5)
        
        for nb in range(len(free_points)):
            if free_points[nb]:
                new_tracker = Tracker(self.current_coordonates[nb],matching_time,)
                

        


        

        


class Tracker():
    def __init__(self,dim):
        self.label = None
        self.last_known_position = [0 for i in dim]
        self.last_known_speed = [0 for i in dim]
        self.last_known_acceleration = [0 for i in dim]
        self.last_time_seen = time.time()
        self.certainty = 0.5

    def __init__(self,original_pos,t,label):
        dim = len(original_pos)
        self.label = label
        self.last_known_position = original_pos
        self.last_known_speed = [0 for i in dim]
        self.last_known_acceleration = [0 for i in dim]
        self.last_time_seen = t
        self.certainty = 0.5

    def estimate_position_at(self,t):
        
        dt = t - self.last_time_seen        
        pos_estimate = self.last_known_position + self.last_known_speed * dt + self.last_known_acceleration * dt *dt * 0.5 
        return pos_estimate
    
    def get_scores(self,coordonates_list, label_list,t):       
        pos_estimate = self.estimate_position_at(t)
        score = []
        for i in range(len(coordonates_list)):
            vect = coordonates_list[i]
            label = label_list[i]
            if self.label == None or self.label == label:
                dist = np.abs(pos_estimate - vect) * self.certainty
            else :
                dist = 999999
            score.append(dist)
        return score

    def update_coordonates(self,new_position, new_time, new_certainty):
        dt = new_time - self.last_time_seen
        new_v = (new_position - self.last_known_position) / dt
        new_a = (new_v - self.last_known_speed) / dt

        self.last_known_acceleration = new_a
        self.last_known_speed = new_v
        self.last_known_position = new_position
        self.last_time_seen = new_time
        self.certainty = new_certainty

    
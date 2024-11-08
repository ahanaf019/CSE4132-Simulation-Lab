import pandas as pd
from typing import List
import math

class Activity:
    def __init__(self, name, start_node, end_node, duration) -> None:
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.duration = duration
        self.pred = []
        self.es = None
        self.ef = None
        self.ls = None
        self.lf = None
        self.slack = None
        self.critical = None
        

def forward_pass(activities: List[Activity]):
    for i in range(len(activities)):
        if activities[i].start_node == 1:
            activities[i].es = 0
            activities[i].ef = activities[i].duration
        
        else:
            st = -1
            for j in range(len(activities)):
                if j == i:
                    continue
                if activities[j].end_node == activities[i].start_node:
                    if activities[j].duration + activities[j].es > st:
                        st = activities[j].duration + activities[j].es
            activities[i].es = st
            activities[i].ef = st + activities[i].duration




# def backward_pass(activities: List[Activity]):
#     lf = 0
#     j = -1
#     for i in range(len(activities)):
#         if activities[i].ef > lf:
#             lf = activities[i].ef
#             j = i
    
#     activities[j].lf = lf
#     activities[j].ls = lf - activities[j].duration
#     activities[j].slack = activities[j].ls - activities[j].es
#     activities[j].critical = ( activities[j].slack == 0 )
    
#     ln = len(activities)
#     while ln > 0:
        
        
#         ln -= 1
    
    
#     for activity in activities:
#         print(activity.name, activity.duration, activity.es, activity.ef, activity.ls, activity.lf, activity.slack, activity.critical)
    


def backward_pass(activities: List[Activity], j):
    # if activities[j].
    pass





df = pd.read_csv('./cpm_data.csv')
activities = []
for i in range(df.shape[0]):
    activity = Activity(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3])
    activities.append(activity)
    
forward_pass(activities)
backward_pass(activities)

# for activity in activities:
#     print(activity.name, activity.duration, activity.es, activity.ef)
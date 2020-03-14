# -*- coding: utf-8 -*-

def intervals(dc):
    interval = [0, 0]
    intervals = []
    flag = 0
    if (dc[0] < 0):
        flag = 1
    
    for i in range(len(dc)):
        if(flag):
            if(dc[i] >= 0):
                interval[0] = i-1
                interval[1] = i
                intervals.append(interval)
                flag = 0
        else:
            if(dc[i] <= 0):
                interval[0] = i-1
                interval[1] = i
                intervals.append(interval)
                flag = 1
    
    return intervals
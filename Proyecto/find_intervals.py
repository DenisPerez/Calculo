# -*- coding: utf-8 -*-

def intervals(dc):
    intervals = []
    flag = 0
    if (dc[0] < 0):
        flag = 1

    for i in range(1,len(dc)):
        if(flag == 1):
            if(dc[i] >= 0):
                intervals.append([i-2,i])
                flag = 0
        else:
            if(dc[i] <= 0):
                intervals.append([i-2,i])
                flag = 1
    
    return(intervals)
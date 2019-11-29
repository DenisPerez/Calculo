# -*- coding: utf-8 -*-
import numpy as np

f = lambda x : (x-np.sin(x))/(x**3)
fvalues = []

def evaluatef(n):
    for x in range(1,n+1):
        if x == 1:
            fvalues.append(f(1))
        else:
            x = (1/10)*x
            fvalues.append(f(x))
        
        
        
    
evaluatef(15)
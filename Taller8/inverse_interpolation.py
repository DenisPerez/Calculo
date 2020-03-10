# -*- coding: utf-8 -*-
import numpy as np
from scipy.interpolate import interp1d

def raiz(alpha):
    a_value = 5 #alpha value
    #interp_fn2 = lambda x : (x)**3 - a_value
    
    #x points for work
    x_points = np.random.uniform(low = -a_value, high = 0.0, size = 30)
    x_points = np.concatenate([x_points, -x_points])
    
    y = (x_points)**3 - a_value #function x^(3) - alpha
    
    interp_fn =  interp1d(y, x_points, kind = 'quadratic', fill_value = 'extrapolate')
    
    root = float(interp_fn(0))
    
    return root
   # prove = interp_fn2(root)

r = raiz(5)






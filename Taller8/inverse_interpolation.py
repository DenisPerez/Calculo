# -*- coding: utf-8 -*-
import numpy as np
from scipy.interpolate import interp1d

def raiz3(alpha):
    #interp_fn2 = lambda x : (x)**3 - a_value
    
    #x points for work
    x_points = np.random.uniform(low = -alpha, high = 0.0, size = 30)
    x_points = np.concatenate([x_points, -x_points])
    
    y = (x_points)**3 - alpha #function x^(3) - alpha
    
    interp_fn =  interp1d(y, x_points, kind = 'quadratic', fill_value = 'extrapolate')
    
    root = float(interp_fn(0))
    #prove = interp_fn2(root)
    return root

r = raiz3(5)






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:03:47 2020

@author: cicore219
"""
import numpy as np
def xHouseholder(e):
    Q = R = np.zeros((3,3))
    Z = 1+(e**2)-((e**4)+2*(e**2)+3)**(1/2)
    n = 6+4*(e**2)+2*(e**4)-2*((e**4)+2*(e**2)+3)**(1/2)-2*(e**2)*((e**4)+2*(e**2)+3)**(1/2)
    a = -(Z**2)/(n**2)
    b = -(Z)/(n**2)
    c = -1/(n**2)
    Q[0][0] = a + b**3 + 2*(b**2) + a*(c**2) + b*(c**2) + (c**2) + 2*a*c + 3*(b**2)*c + 3*a*b*c + 4*b*c + 2*c + 1
    Q[0][1] = (b**3) + 2*(b**2) + 2*a*b + 2*b + a*(c**2) + b*(c**2) + (c**2) + a*c + 3*(b**2)*c + 3*a*b*c + 3*b*c + c
    Q[0][2] =  2*(b**3) + 3*a*(b**2) + 
    
    return x

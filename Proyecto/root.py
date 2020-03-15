# -*- coding: utf-8 -*-
import numpy as np

def L1 (x):
    return (p1*h1/np.math.sqrt((h1**2 + x**2)**3))

def L2(x):
    return (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

def Cx (x):
    return -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

def bisection(a,b, tol):
    
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        
        c = (xl+xr)/2.0
        prod = Cx(xl) * Cx(c)
        
        if prod > tol:
            xl = c
            
        else:
            if prod < tol:
                xr = c
        
    return c


def intersection(a,b, tol):
    
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        
        c = (xl+xr)/2.0
        minus = L1(xl) - L2(c)
        
        if minus > tol:
            xl = c
            
        else:
            if minus < tol:
                xr = c
        
    return c
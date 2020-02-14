# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp

p2 = lambda x, a, b : a*x + b

def sumlists(listx, listy):
    return [ listx[i]*listy[i] for i in range(4) ]

def rectaLSP(x,y):
    A = np.zeros((2,2), dtype=float)
    b = np.zeros((2,1), dtype=float)
    
    A[0][0] = sum(x**2 for x in range(4))
    A[0][1] = sum(x)
    A[1][0] = sum(x)
    A[1][1] = 2
    
    b[0][0]= sum(sumlists(x,y))
    b[1][0]= sum(y)
    
    x1 = np.linalg.solve(A,b)
    
    a = x1[0][0]
    b = x1[1][0]
    r = 0
    
    for i in range(4):
        r = (p2(x[i],a,b) - y[i])**2
    return x1, r
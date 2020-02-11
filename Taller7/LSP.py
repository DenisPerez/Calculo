# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp

def sumlists(listx, listy):
    return [ listx[i]*listy[i] for i in range(4) ]

x = [0,1,2,3]
y = [4,5,8,13]

A = np.zeros((2,2), dtype=float)
b = np.zeros((2,1))

A[0][0] = sum(x**2 for x in range(4))
A[0][1] = sum(x)
A[1][0] = sum(x)
A[1][1] = 4

w = sumlists(x,y)
b[0][0]= sum(sumlists(x,y))
b[1][0]= sum(y)

x = np.linalg.solve(A,b)
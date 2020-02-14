# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp
from recta_lsp import rectaLSP
import matplotlib.pyplot as plt

p2 = lambda x, a, b, c : a*(x**2) + b*x + c

def sumlists(listx, listy):
    return [ listx[i]*listy[i] for i in range(4) ]

def parabola2LSP(x,y):
    A = np.zeros((3,3), dtype=float)
    b = np.zeros((3,1), dtype=float)
    
    A[0][0] = sum(x**4 for x in range(4))
    A[0][1] = sum(x**3 for x in range(4))
    A[0][2] = sum(x**2 for x in range(4))
    A[1][0] = A[0][1]
    A[1][1] = A[0][2]
    A[1][2] = sum(x)
    A[2][0] = sum(x**2 for x in range(4))
    A[2][1] = sum(x)
    A[2][2] = 4
    
    b[0][0] = sum(sumlists([x**2 for x in range(4)],y))
    b[1][0] = sum(sumlists(x,y))
    b[2][0] = sum(y)
    
    x1 = np.linalg.solve(A,b)
    
    a = x1[0][0]
    b = x1[1][0]
    c = x1[2][0]
    r = 0
    for i in range(4):
        r = (p2(x[i],a,b,c) - y[i])**2
    return x1 , r
# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp
from recta_lsp import rectaLSP
import matplotlib.pyplot as plt

def sumlists(listx, listy):
    return [ listx[i]*listy[i] for i in range(4) ]

x = [0,1,2,3]
y = [4,5,8,1]

A = np.zeros((3,3), dtype=float)
b = np.zeros((3,1))

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

x = np.linalg.solve(A,b)
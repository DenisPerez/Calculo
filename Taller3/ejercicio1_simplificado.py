# -*- coding: utf-8 -*-

from pprint import pprint
import numpy as np

n = 10000
y = lambda i, j: -1 if i < j  else 1
L_function = lambda i,j: 2 if (i==j and i != (n-1)) else (y(j,i) if i == (n-1) else 0)
U_function = lambda i,j: 0 if i < j else (1 if (i == j or i == (n-1)) else 0.5) 

L = [[L_function(j,i) for i in range(n)] for j in range(n)]
U = [[U_function(i,j) for i in range(n)] for j in range(n)]

print("L: \n")
pprint(np.array(L))
print("\n")
print("U: \n")
pprint(np.array(U))
print("\n")
print("A = UL: \n")
pprint(np.dot(U,L))
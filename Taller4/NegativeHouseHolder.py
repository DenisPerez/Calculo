# -*- coding: utf-8 -*-

from pprint import pprint # pretty print import
import numpy as np # numyp import
from numpy import finfo # Epsilon import
from numpy import eye #Eye function import
from numpy import sqrt #Square root import
from numpy.random import randn #random library

# -*- coding: utf-8 -*-

I = np.identity(6)
#this function return the norm of a vector

def norm(x):
    return np.linalg.norm(x)

def cmp(obj1, obj2):
    if obj1 < obj2:
        return -1
    elif obj1 == obj2:
        return 0
    elif obj1 > obj2:
        return 1
    
def NegativeHouseHolder(A,e):

    alpha = -cmp(A[0][0],0) * norm(A)
    pprint(A)
    print("\n")
    print(alpha)
    print("\n")
    e[0][0] = alpha
    #pprint(A)
    pprint(e)
    
    #print(e)
    u = A + e
    pprint(u)
    print("\n")

    norm_u = norm(u)
    #pprint(norm_u)
    v = 2/norm_u**2
    
    V = v * np.dot(u,u.transpose())
    #pprint(V)
    H = np.subtract(I,V)
    pprint(H)
    print("\n")
    pprint(np.dot(H,A))
    print("\n")
    e[0][0] = alpha
    pprint(e)

#PositiveHouseHolder(x1,e1)
# -*- coding: utf-8 -*-


import numpy as np # numyp import
from numpy import finfo # Epsilon import
from numpy import eye #Eye function import
from numpy import sqrt #Square root import
from numpy.random import randn #random library
from pprint import pprint


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

    alpha = np.sign(A[0][0]) * norm(A)
    e[0][0] = alpha

    u = A + e

    norm_u = norm(u)
    
    v = 2/norm_u**2
    
    V = v * np.dot(u,u.transpose())
    
    H = np.subtract(I,V)

    e[0][0] = alpha
    
    return (H,alpha) #Retorno la matriz H y el alpha perteneciente a los vectores
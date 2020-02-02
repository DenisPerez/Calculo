# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:09:36 2019

@author: gata
"""

import scipy as sp
import scipy.linalg as sla
import numpy as np
from ejercicio3_MatrizSPD import ASPD as SPD

def GaussSeidel(A,x,b,tol,maxiter):
    n=len(b)
    r=[0.0 for i in range(maxiter+1)]
    r[0] = sla.norm(b-sp.dot(A,x))
    for k in range(maxiter):
        for i in range(n):
            s1=0.0
            for j in range(n):
                if i != j:
                    s1 = s1 + A[i][j]*x[j]                    
            x[i] =(b[i] -s1)/A[i][i]
        r[k+1] = sla.norm(b - sp.dot(A,x))
        if r[k+1]<tol:
            break
    return x,k,r
"""
A = np.array([[2.2542 ,   0.202523  ,  -0.834092   , 0.227431],
[0.202523 ,   3.74738 ,   -0.0865564  ,  -0.618917],
[-0.834092  ,  -0.0865564   , 1.56507 ,   -0.271188],
[0.227431 ,   -0.618917   , -0.271188  ,  2.43336]])
b = np.array([1.,]*4).reshape(4,1)
x = np.zeros_like(b)
tol = 0.001
maxiter = 500
sol,pa,r = GaussSeidel(A,x,b,tol,maxiter)
"""
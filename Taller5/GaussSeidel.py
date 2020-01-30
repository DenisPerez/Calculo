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
n = 2
b = np.array([[1]*n]).transpose()
b1 = np.array([[1]*n]).transpose()
x = np.array([[0]*n], dtype = float).transpose()
x1 = np.array([[0]*n]).transpose()
max_iteraciones = 500
tol = 0.0001
A = SPD(n)
solucion1, pasos, residual1 = GaussSeidel(A,x,b,tol,max_iteraciones)

solucion1, pasos, residual1 = GaussSeidel(A,x,b,tol,max_iteraciones)
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])

x = np.zeros_like(b)
#solucion1, pasos, residual1 = GaussSeidel(A,x,b,tol,max_iteraciones)
"""
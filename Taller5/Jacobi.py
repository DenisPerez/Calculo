# -*- coding: utf-8 -*-

import scipy as sp
import scipy.linalg as sla
from ejercicio3_MatrizSPD import ASPD as SPD
import numpy as np


def Jacobi(A,x,b,tol,maxiter):
    n=len(b)
    r=[0.0 for i in range(maxiter+1)]
    r[0] = sla.norm(b-sp.dot(A,x))
    for k in range(maxiter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        r[k+1] = sla.norm(sp.dot(A,x)-b)
        if r[k+1]<tol:
            break
        x = x_new
    return x_new,k,r

"""
n = 5
b = np.array([[1]*n]).transpose()
b1 = np.array([[1]*n], dtype = float).transpose()
x = np.array([[0]*n]).transpose()
x1 = np.array([[0]*n]).transpose()
max_iteraciones = 500
A = SPD(n)
tol = 0.0001

solucion1, pasos, residual1 = Jacobi(A,x,b,tol,max_iteraciones)
solucion1, pasos, residual1 = Jacobi(A,x,b,tol,max_iteraciones)
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])

x = np.zeros_like(b)
solucion1, pasos, residual1 = Jacobi(A,x,b,tol,max_iteraciones)
"""
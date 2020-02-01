# -*- coding: utf-8 -*-

import scipy as sp
import scipy.linalg as sla

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

A = np.array([[2.2542 ,   0.202523  ,  -0.834092   , 0.227431],
[0.202523 ,   3.74738 ,   -0.0865564  ,  -0.618917],
[-0.834092  ,  -0.0865564   , 1.56507 ,   -0.271188],
[0.227431 ,   -0.618917   , -0.271188  ,  2.43336]])
b = np.array([1.,]*4).reshape(4,1)
x = np.zeros_like(b)
tol = 0.001
maxiter = 500
sol2, pas2, r2 = Jacobi(A,x,b,tol,maxiter)
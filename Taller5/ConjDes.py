# -*- coding: utf-8 -*-

import scipy as sp
import scipy.linalg as sla
import numpy as np
from ejercicio3_MatrizSPD import ASPD as SPD
def ConjDes(A,xk,b,tol,maxiter):
    r=[0.0 for i in range(maxiter+1)]

    pk = b-sp.dot(A,xk) #r
    u = pk #p
    r[0] = sla.norm(pk) #r_k_norm
    for k in range(maxiter):
       wk = sp.dot(A,u) #Ap
       tk = (sla.norm(pk)**2)/sp.dot(sp.transpose(u),wk) #alpha
       xk = xk + tk*u
       pk_plus1 = pk - tk*wk
       r[k+1] = sla.norm(pk_plus1)
       beta = (sla.norm(pk_plus1)**2) / (sla.norm(pk)**2)
       u = pk_plus1 + beta * u
       pk = pk_plus1
       if r[k+1]<tol:
            break
    return xk,k,r
"""
A = np.array([[2.2542 ,   0.202523  ,  -0.834092   , 0.227431],
[0.202523 ,   3.74738 ,   -0.0865564  ,  -0.618917],
[-0.834092  ,  -0.0865564   , 1.56507 ,   -0.271188],
[0.227431 ,   -0.618917   , -0.271188  ,  2.43336]])
b = np.array([1.,]*4).reshape(4,1)
x = np.zeros_like(b)
tol = 0.001
maxiter = 500
sol13,pa13,r13 = ConjDes(A,x,b,tol,maxiter)
"""
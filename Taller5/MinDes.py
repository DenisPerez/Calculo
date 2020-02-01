# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:41:46 2019

@author: gata
"""
import scipy as sp
import scipy.linalg as sla
import numpy as np
from ejercicio3_MatrizSPD import ASPD as SPD
def MinDes(A,xk,b,tol,maxiter):
    r=[0.0 for i in range(maxiter+1)]
    
    pk = b-sp.dot(A,xk)
    r[0] = sla.norm(pk)
    for k in range(maxiter):
       wk = sp.dot(A,pk)
       tk = (sla.norm(pk)**2)/sp.dot(sp.transpose(pk),wk)
       xk = xk + tk*pk;
       pk = pk - tk*wk;
       r[k+1] = sla.norm(pk)
       if r[k+1]<tol:
            break
    return xk,k,r

A = np.array([[2.2542 ,   0.202523  ,  -0.834092   , 0.227431],
[0.202523 ,   3.74738 ,   -0.0865564  ,  -0.618917],
[-0.834092  ,  -0.0865564   , 1.56507 ,   -0.271188],
[0.227431 ,   -0.618917   , -0.271188  ,  2.43336]])
b = np.array([1.,]*4).reshape(4,1)
x = np.zeros_like(b)
tol = 0.001
maxiter = 500
sol1,pa1,r1 = MinDes(A,x,b,tol,maxiter)
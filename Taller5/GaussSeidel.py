# -*- coding: utf-8 -*-

import scipy as sp
import scipy.linalg as sla
from ejercicio3_MatrizSPD import ASPD as SPD
import numpy as np

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
            x[i] =(b[i] - s1)/A[i][i]
        r[k+1] = sla.norm(b-sp.dot(A,x))
        if r[k+1]<tol:
            break
    return x,k,r



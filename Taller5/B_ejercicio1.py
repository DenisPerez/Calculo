# -*- coding: utf-8 -*-

import numpy as np

import scipy.linalg as sla


def B(A,I,Q,R):
    n,m = A.shape
    
    #Q, R = np.linalg.qr(A)
    
    Q = Q.T
    B = np.empty([n,m])
    for i in range(n):
        e = I[:,i].reshape(n,1)
        x = RxQTb(R,Q,e)
        B[:,i:i+1] = x
        
    return B


def RxQTb(R,Q,b): #esta funcion hace la resolucion del sistema Rx = Q.T b
        
    b = Q @ b
    return sla.solve(R,b, sym_pos=False, lower=False)
    

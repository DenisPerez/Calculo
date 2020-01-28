# -*- coding: utf-8 -*-

import scipy as sp
import scipy.linalg as sla

def ASPD(n):
    Q = sp.rand(n,n)
    Q,R = sla.qr(Q)
    D = [[0.0]*n for i in range(n)]
    for i in range(n):
        D[i][i] = i+1
    A = sp.dot(sp.dot(Q,D), sp.transpose(Q)) #A = Q*D*Q^t
    return A
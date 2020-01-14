# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:08:39 2020

@author: Usuario
"""

from pprint import pprint
import scipy.linalg as sla
import numpy as np

n = 3
MaxIter = 10

def fact():
    A = np.random.randn(n,n)
    A = (A + A.transpose())*(1/2)
    Q_ = np.identity(n)
    T = A
    #print("A:")
    #pprint(A)
    for k in range(MaxIter):
        Q, R = np.linalg.qr(T)
        T = np.dot(R,Q)
        Q_ = np.dot(Q_,Q)
    
    #print()
    #pprint(Q)
    #pprint(R)
    print("T:")
    pprint(T)
    print("Autovalores de A: ")
    eigvals, _ = sla.eig(A)
    print(eigvals)
    #M = T - np.dot(Q_.transpose(), (np.dot(A,Q_)))
    #c = np.linalg.norm(M,2)
    #print("norma 2: ")
    #print(c)
    #inversa = sla.inv(T)
    #print("inversa de T: ")
    #pprint(inversa)
    
fact()
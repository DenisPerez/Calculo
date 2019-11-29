# -*- coding: utf-8 -*-
import numpy as np

A = np.array([[0.4,-0.6,0.2],[-0.3,0.7,-0.4],[-0.1,-0.4,0.5]])
x = np.array([[1],[1],[1]])

normainf = lambda x : np.linalg.norm(x,ord = np.inf)
Cociente_de_Rayleigh = lambda x, A : np.dot(np.transpose(x),np.dot(A,x))/(np.dot(np.transpose(x),x))

def potencia(A,x, MaxIter):
    for k in range(1,MaxIter+1):
        x = np.dot(A,x)
        x = x / normainf(x)
    return (Cociente_de_Rayleigh(x,A))

print(potencia(A,x,500))
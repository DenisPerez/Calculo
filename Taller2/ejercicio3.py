# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import scipy as s

A = np.array([[0.4,-0.6,0.2],[-0.3,0.7,-0.4],[-0.1,-0.4,0.5]])
x = np.array([[1],[1],[1]])


def potencia(A,x, MaxIter):
    for k in range(1,MaxIter):
        x = np.dot(A,x)
        x = x/(np.linalg.norm(x,ord = np.inf))
    return (np.dot(np.transpose(x),np.dot(A,x))/(np.dot(np.transpose(x),x)))

print(potencia(A,x,500))
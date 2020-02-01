 #-*- coding: utf-8 -*-

import scipy as sp
from Jacobi import Jacobi as JA
from GaussSeidel import GaussSeidel as GA
from ejercicio3_MatrizSPD import ASPD as SPD
from matplotlib import pyplot as plt
import numpy as np

n = 100
b = np.array([[1.]*n]).transpose()
b1 = np.array([[1]*n]).transpose()
x = np.array([[0]*n], dtype = float).transpose()
x1 = np.array([[0]*n], dtype=float).transpose()
A = SPD(n)
tol = 0.001
max_iteraciones = 500
xticks1 = sp.linspace(0,max_iteraciones,max_iteraciones+1).reshape(max_iteraciones+1,1)
fig, ax = plt.subplots(2,1)

solucion1, pasos1, residual1 = GA(A,x,b,tol,max_iteraciones)
solucion2, pasos2, residual2 = JA(A,x1,b1,tol,max_iteraciones)

ax[0].plot(xticks1, residual1)
ax[0].set_ylabel('$ |b - Ax|\ $')
ax[1].plot(xticks1, residual2)
ax[1].set_xlabel("Numero de iteraciones")
ax[1].set_ylabel('$ |b - Ax|\ $')
fig.align_ylabels()
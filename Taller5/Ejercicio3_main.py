 #-*- coding: utf-8 -*-

import scipy as sp
from Jacobi import Jacobi as JA
from GaussSeidel import GaussSeidel as GA
from ejercicio3_MatrizSPD import ASPD as SPD
from matplotlib import pyplot as plt
import numpy as np


n = 500
b = np.array([[1]*n]).transpose()
x = np.array([[0]*n]).transpose()
A = SPD(n)
tol = 0.001
max_iteraciones = 500


xticks1 = sp.linspace(1,500,500+1).reshape(501,1)
xticks2 = sp.linspace(1,500,500+1).reshape(501,1)
fig, ax = plt.subplots(2,1)

solucion, pasos, residual = GA(A,x,b,tol,max_iteraciones)
ax[0].plot(xticks1, residual, 'o-')
ax[0].set_title = ("r de GaussSeidel vs Residuo Jacobi")
ax[0].set_ylabel("r GaussSeidel en escala lineal")

solucion, pasos, residual = JA(A,x,b,tol,max_iteraciones)
ax[1].plot(xticks2, residual, '.-')
ax[1].set_xlabel("Numero de iteraciones")
ax[1].set_ylabel("r Jacobi.py en escala lineal")

plt.show()

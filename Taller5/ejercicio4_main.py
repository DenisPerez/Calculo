# -*- coding: utf-8 -*-
from MinDes import MinDes
from ConjDes import ConjDes
from GaussSeidel import GaussSeidel
from ejercicio3_MatrizSPD import ASPD as SPD
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp

n = 100
b = np.array([[1.]*n]).transpose()
b1 = np.array([[1]*n]).transpose()
b2 = np.array([[1]*n]).transpose()
x = np.array([[0]*n], dtype = float).transpose()
x1 = np.array([[0]*n], dtype=float).transpose()
x2 = np.array([[0]*n], dtype=float).transpose()
A = SPD(n)
tol = 0.001
max_iteraciones = 500

xticks1 = sp.linspace(0,max_iteraciones,max_iteraciones+1).reshape(max_iteraciones+1,1)
fig = plt.figure()
ax1 =  fig.add_axes([0.1,0.1,0.8,0.8])
sol, pas, r = GaussSeidel(A,x,b,tol,max_iteraciones)
sol1, pas1, r1 = MinDes(A,x1,b1,tol,max_iteraciones)
sol2, pas2, r2 = ConjDes(A,x2,b2,tol,max_iteraciones)
ax1.grid()
ax1.plot(r,'r', label='$GaussSeidel$')
ax1.plot(r1,'b' ,label='$MinDes$')
ax1.plot(r2,'m' ,label='$ConjDes$')
ax1.set_xlabel('iteraciones')
ax1.set_title('$GaussSeidel vs MinDes vs ConjDes$')
ax1.legend(loc=0)
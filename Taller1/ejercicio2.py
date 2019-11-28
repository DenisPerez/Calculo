# -*- coding: utf-8 -*-

from matplotlib import pyplot as mt
import random

from time import time

timefila = [] #TIEMPO CONSUMIDO POR CADA UNA DE LAS MATRICES AL SER COMPUTADAS POR MatVecFila HASTA LLEGAR A num_iteraciones
timecolumna=[]#TIEMPO CONSUMIDO POR CADA UNA DE LAS MATRICES  AL SER COMPUTADAS POR MatVecCol HASTA LLEGAR A num_iteraciones
C = []
num_iteraciones = 600  # TAMANO MAXIMO DE MATRIZ 

mt.rcParams.update({'figure.figsize': [8,6],'font.size': 18, 'font.family': 'serif'})

def MatVecFila(A,x):
    for i in range(len(A)):
        acum=0
        for j in range(len(A[i])):
            acum+=A[i][j]*x[j]
        C.append(acum)
    
def MatVecCol(A,x):
    for i in range(len(A[0])):
        for j in range(len(A)):
            A[j][i] = A[j][i] * x[i]
    for k in range(len(A)):
        C.append(sum(A[k]))
        
def MatMatFormakji(A, x,C):
    for k in range(len(x)):
        for j in range(len(x[0])):
            for i in range(len(A)):
                C[i][j] = C[i][j] + A[i][k]*x[k][j]
    

for w in range(100, num_iteraciones):
    start_time = time()
    A = [[random.randint(-400,1000) for i in range(w)]for j in range(w)]
    x = [i+1 for i in range(w)]
    MatVecFila(A,x)
    timefila.append(time()-start_time)

C = []
for w in range(100, num_iteraciones):
    start_time = time()
    A1 = [[random.randint(-400,1000) for i in range(w)]for j in range(w)]
    x1 = [i+1 for i in range(w)]
    MatVecCol(A1,x1)
    timecolumna.append(time()-start_time)
    
#Graficacion
fig = mt.figure()
ax1 =  fig.add_axes([0.1,0.1,0.8,0.8])
ax1.grid()
ax1.plot(timefila,'r', label='$MatVecFila$')
ax1.plot(timecolumna,'m' ,label='$MatVecCol$')
ax1.set_xlabel('iteraciones')
ax1.set_ylabel('tiempo')
ax1.set_title('$MatVecFila \quad vs \quad MatVecColumna$')
ax1.legend(loc=0)


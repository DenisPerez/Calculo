# -*- coding: utf-8 -*-

from matplotlib import pyplot as mt
import numpy as np
import scipy as s
import random
from time import time

time_kji = []
timeijk = []

def MatMatFormakji(A, x):
    
    C = [[0 for i in range(n)] for j in range(m)]
    start_time = time()
    for k in range(len(x)):
        for j in range(len(x[0])):
            for i in range(len(A)):
                C[i][j] = C[i][j] + A[i][k]*x[k][j]
    time_kji.append(time()-start_time)

                
def MatMatijk(A,x):
    start_time = time()
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(len(A)):
        for j in range(len(x[0])):
            for k in range(len(x)):
                C[i][j] = C[i][j] + A[i][k] * x[k][j]
    timeijk.append(time()-start_time)
                
    
for i in range(100,400):
    p = random.randint(100,150)
    m = random.randint(100,150)
    n = random.randint(100,150)
    A = [[random.randint(-400,1000) for i in range(p)]for j in range(m)]
    B = [[random.randint(-400,1000) for i in range(n)] for j in range(p)]
    MatMatFormakji(A,B)
    MatMatijk(A,B)
"""
for i in range(100,150):
    p = random.randint(100,150)
    m = random.randint(100,150)
    n = random.randint(100,150)
    A = [[random.randint(-400,1000) for i in range(p)]for j in range(m)]
    B = [[random.randint(-400,1000) for i in range(n)] for j in range(p)]
    MatMatijk(A,B)
"""
fig = mt.figure()
ax1 =  fig.add_axes([0.1,0.1,0.8,0.8])
ax1.grid()
ax1.plot(time_kji,'r', label='$kji$')
ax1.plot(timeijk,'m' ,label='$ijk$')
ax1.set_xlabel('iteraciones')
ax1.set_ylabel('tiempo')
ax1.set_title('$MatMatFormaijk vs MatMatFormakji$')
ax1.legend(loc=0)

mt.savefig('kji.png')
mt.savefig('kji.pdf')
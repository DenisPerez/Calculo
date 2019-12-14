# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:32:42 2019

@author: Usuario
"""

import scipy as s
import numpy as np
from pprint import pprint

def PA(A):
    P = []
    L = []
    n = len(A)
    for i in range(n-1):
        ind = i
        mayor = s.absolute(A[i][i])
        for j in range(i,n):
            if s.absolute(A[j][i]) > mayor:
                #Es necesario cambiar de pivote
                mayor = s.absolute(A[j][i])
                ind = j
        #Sacar Pi
        Pi = np.identity(n)
        Pi[[i, ind]] = Pi[[ind, i]]
        P.append(Pi)
        #Cambio de pivote
        temp = A[i]
        A[i] = A[ind]
        A[ind] = temp
            
        #Sacar Li
        Li = np.identity(n)
        for k in range(i+1,n):
            multiplicador = A[k][i]/A[i][i]
            Ei = np.identity(n)
            Ei[k][i] = -1*multiplicador
            A[k][i] = 0
            for z in range(i+1,n):
                A[k][z] = A[k][z]-multiplicador*A[i][z]
            Li = np.matmul(Li,Ei)
        L.append(Li)
        
    for i in range(n-1):
        print("Paso: ",i+1,"\n")
        print("P",i+1,"\n")
        pprint(P[i])
        print("L",i+1,"\n")
        pprint(L[i])
        print("\n\n")
        
M = [[-2,5,7,4], [7,1,-10,1], [4,8,-4,9], [3,12,1,-8]]
#M = [[0,0,2],[-1,5,-2],[3,6,7]]
#M = [[0,1,1],[-1,2,-4],[2,-5,1]]
#M = [[2,-2,1],[-8,11,5],[4,-13,3]]
#M = [[1,4,0,-4],[5,1,1,-1],[3,1,-1,-2],[-3,4,6,2]]
PA(M)
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:19:00 2019

@author: gata
"""
import scipy as s

def factLU(A):
    n=len(A)
    for k in range(n-1):
        if s.absolute(A[k][k])<1e-20:
            print('Pivote cercano a cero en k=%d' % k)
            L=[[0.0]*n for i in range(n)]
            U=[[0.0]*n for i in range(n)]
            return L,U
        else:
            for i in range(k+1,n):
                A[i][k] = A[i][k]/A[k][k]
                for j in range(k+1,n):
                    A[i][j] = A[i][j]-A[i][k]*A[k][j]

    #==================================
    #OBSERVE QUE: 
    #Las siguientes lineas en realidad no hacen falta
    U=s.triu(A)
    L=s.tril(A,-1)
    for i in range(n):
        L[i][i] =1.0
    return L,U
    #==================================

M=[[1,2,4,5], [3,4,7,3], [9,-1,5,5], [-3, 6, -1,2]]
n=4
L,U=factLU(M)

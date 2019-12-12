# -*- coding: utf-8 -*-

from pprint import pprint

A = [[1,2,3],[4,5,7],[9,8,7]]

def factLUBack(A):
    
    n = len(A)
    
    for k in range(n-1, -1, -1):
        for i in range(k-1, -1, -1):
            #print(A[i][k])
            A[i][k] = A[i][k]/A[k][k]
            #print(A[k][k])
            
            for j in range(k-1, -1, -1):
                #print(A[i][j])
                A[i][j] = A[i][j]-A[i][k]*A[k][j]
                #print(A[i][j])
            #print("\n")
    
    return(A)
    
U = factLUBack(A)
pprint(U)
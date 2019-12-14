# -*- coding: utf-8 -*-

from pprint import pprint
import numpy as np
from upper_lower import upper, lower

#Number of rows and columns off the matrix A
n = 10
#FUNCION LAMBDA PARA CREAR MATRICES DE LA FORMA PARTICULAR DE LA PREGUNTA
y = lambda i, j: -1 if i < j  else (1 if i == j or i == (n-1)  else 0)
#z = lambda i,j: 1 if i == j else 0
#CREACION DE LA MATRIZ A
A = [[y(i,j) for i in range(n)]for j in range(n)]
def factLUBack(A):
    n = len(A)
    for k in range(n-1, -1, -1):
        for i in range(k-1, -1, -1):
            A[i][k] = A[i][k]/A[k][k]
            for j in range(k-1, -1, -1):
                A[i][j] = A[i][j]-A[i][k]*A[k][j]
    return(np.array(A))

matrix = factLUBack(A)
#pprint(matrix)
L = lower(matrix,n,n)
U = upper(matrix,n,n)

print("L:")
pprint(L)
print("\n")
print("U:")
pprint(U)
print("\n")
print("A = UL:")
pprint(np.dot(U,L))
# -*- coding: utf-8 -*-

import scipy.linalg as sla
from math import sqrt
from pprint import pprint
import numpy as np


def cholesky(A):
    n = len(A) #tamano de la matriz a procesar
    
    L = [[0.0]* n for i in range(n)]#iniciaizo L como una matriz de todo 0
    
    
    for i in range(n):
        for k in range(i+1):  
            back_list = [L[i][j] * L[k][j] for j in range(k)]
            tmp_sum = sum(back_list)
            if (i==k):
                #Me encuentro en una diagonal y por lo tanto solo tengo que elevar al cuadrado
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                #Tengo que restar todos los elementos anteriores al valor de A y tengo que sacar raiz
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return (np.array(L)).transpose()#Retorno la matriz traspuesta para comprobar los resultados
                                    #Con la matriz resultante de sla.cholesky

# Matrices de la practica para los ejemplos
#A = np.array([[4,1,-1], [-1,4.25,2.75], [1,2.75,4]])
#A = np.array([[25,25,25],[25,50,50],[25,50,75]])
A = np.array([[25,-25,-25],[-25,50,0],[-25,0,75]])
#A = np.array([[25,25,25],[25,106,106],[25,106,6667]])
#A = np.array([[4,-6,14],[-6,34,-34],[14,-34,339]])

L = cholesky(A)


print ("A:")
pprint(A)
print("L:")

pprint(L)
print("\n")
L = sla.cholesky(A)
pprint(L)
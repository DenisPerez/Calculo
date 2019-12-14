# -*- coding: utf-8 -*-

import numpy as np

#FFUNCION LAMBDA PARA INICIALIZAR UNA MATRIZ IDENTIDAD
z = lambda i,j: 1 if i == j else 0

#FUNCION PARA CONVERTIR UNA MATRIZ EN TRIANGULAR INFERIOR
def lower(matrix, row, col):
    L = [[0 for i in range (len(matrix))] for j in range (len(matrix))]
    for i in range(0,row):
        
        for j in range(0,col):
          
            if(i >= j):
                
                L[i][j] = matrix[i][j]
    return np.array(L)


#FUNCION PAR ACONVERTIR UNA FUNCION EN TRIANGULAR SUPERIOR
def upper(matrix, row, col):
    U = [[z(i,j) for i in range (len(matrix))] for j in range (len(matrix))]
    for i in range(0,row):
        
        for j in range(0,col):
            
            if(i < j):
                
                U[i][j] = matrix[i][j]
                
    return np.array(U)
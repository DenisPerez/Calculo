# -*- coding: utf-8 -*-

import numpy as np # numpy import
from pprint import pprint

A = np.array([[-2,5,7,4],
              [7,1,-10,1],
              [4,8,-4,9],
              [3,12,1,8]],dtype = 'float64')

(num_rows, num_cols) = np.shape(A)

def MatVecHH(a,u):
    
    ut_a = np.dot(u.transpose() , a)
    ut_u = np.dot(u.transpose() , u)
    p = (2 * ut_a)/ut_u
    
    return a - (p*u)
    
    #retorna un vector columna


def MatMatHH(A,u):
    for i in range(num_cols):
        
        A.transpose()[i] = MatVecHH(np.array([A[:,i]]).transpose(), u).transpose()
        
    return(A)
    #retorna la matriz A
    
T = np.empty([num_rows,num_cols])


#Matriz A

for cont in range(len(A[0]-1)):
    x = np.array([A[cont:, cont]]).transpose()
    e1 = np.eye(len(x),1)
    u = x + np.sign(x[0][0])*np.linalg.norm(x)*e1

    x1 = MatVecHH(x,u)
    if(len(x1) != num_rows):
        N = num_rows - len(x1)
        for i in range(N):
            p = np.zeros(1)
            x1 = np.append(x1,p)
        x1 = np.reshape(x1,(num_cols,1))
        x1 = x1[::-1]
    
    T[:,cont:cont+1] = x1

    
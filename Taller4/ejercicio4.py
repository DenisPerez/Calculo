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
    

T = np.zeros((num_rows,num_cols-1))
    
w = np.array([[8.83176087e+00],
       [8.88178420e-16],
       [4.44089210e-16],
       ])
    
T = list()
T.append(w)

w = np.array([[8.83176087e+00],
       [8.88178420e-16],
       [4.44089210e-16],
       123])
    
T.append(w)
np.vstack(T)
#Matriz A

pprint(y)

for cont in range(len(A[0]-1)):
    x = np.array([A[cont:, cont]]).transpose()
    e1 = np.eye(len(x),1)
    u = x + np.sign(x[0][0])*np.linalg.norm(x)*e1
    
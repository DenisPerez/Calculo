# -*- coding: utf-8 -*-

import numpy as np # numpy import
from pprint import pprint

def MatVecHH(a,u):
    
    ut_a = np.dot(u.transpose() , a)
    ut_u = np.dot(u.transpose() , u)
    p = (2 * ut_a)/ut_u
    
    return a - (p*u)
    #retorna un vector columna


def MatMatHH(A,u):
    for i in range(len(A[0])):
        
        A.transpose()[i] = MatVecHH(np.array([A[:,i]]).transpose(), u).transpose()
        
    return(A)
    #retorna la matriz A
    

A = np.array([[-2,5,7,4],[7,1,-10,1],[4,8,-4,9],[3,12,1,8]],dtype = 'float64')
#Matriz A
x = np.array([A[:,0]]).transpose()
#Vector X traspuesto
e1 = np.eye(len(x),1)
#vector canonico de dimenson de x
u = x + np.sign(x[0][0])*np.linalg.norm(x)*e1
#genero U
#pprint(MatVecHH(x,u))

pprint(MatMatHH(A,u))
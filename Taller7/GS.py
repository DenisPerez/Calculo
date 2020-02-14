# -*- coding: utf-8 -*-
import numpy as np
def gs(A):
    m = np.shape(A)[0]
    n = np.shape(A)[1]
    Q =  np.zeros((m, m))
    R =  np.zeros((n, n)) 
    print (m,n,Q,R)
    for j in range(n):
        v = A[:,j]
        for i in range(j):
            R[i,j] =  np.dot(Q[:,i].T , A[:,j])   # I made an arbitrary change here!!!
            v = v.squeeze() - (R[i,j] * Q[:,i])
        R[j,j] =  np.linalg.norm(v)
        Q[:,j] = (v / R[j,j]).squeeze()
    return Q, R

As = np.array([[1,1,1],[1,0,0],[0,1,0],[0,0,1]])
Q,R = gs(As)

#Elimina una columna de la matriz 
print(np.delete(Q,3,0))

#print(Q@R)
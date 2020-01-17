# -*- coding: utf-8 -*-

import numpy as np # numpy import
from pprint import pprint

"""
def ProdHi(T):
    num_rows, num_cols = T.shape
    u1 = np.array([T[0:, 0]])
    W = np.empty([num_rows,num_cols-1])
    Y = np.empty([num_rows,num_cols-1])
    p = np.zeros(num_cols)
    p[0] = -2/np.dot(u1[0].transpose(), u1[0])
    W = np.dot(p[0], u1[0])
    Y = u1[0]
    for j in range(1, num_cols):
        p[j] = -2/np.dot(u1[j].transpose(), u1[j])
        z = p[j]*(u1[j] + np.dot(W, np.dot(Y.transpose(), u1[j])))
        aux = W.transpose()
        aux[::][-1] = z
        W = aux.transpose()
        aux = Y.transpose()
        aux[::][-1] = u1[j]
        Y = aux.transpose()
    Q = np.identity(num_cols) + np.dot(W, Y.transpose())
    return Q
"""

def ProdHi(T):
    (num_rows, num_cols) = np.shape(T)

    
    W = np.empty([num_rows,num_cols-1])
    Y = np.empty([num_rows,num_cols-1])
    
    u1 = np.array([T[0:, 0]])
    
    p1 = -2/(np.dot(u1.transpose(),np.matrix.conjugate(np.array(u1))))
    
    tt = np.dot(p1,u1.transpose())
    W[:,0:1] = tt.reshape(num_rows,1)
    Y[:,0:1] = u1.reshape(num_rows,1)
    
    for j in range(1,num_cols):
        u1 = np.array([T[j:, j]])
        
        p = -2/(np.dot(u1.transpose(),np.matrix.conjugate(np.array(u1))))
        print(np.shape(u1))
        print(np.shape(Y))
        print(np.shape(W))
        print(np.shape(p))
        WYuj = np.dot(W.transpose(), np.dot(np.matrix.conjugate(Y), u1.transpose()))
        print(np.shape(WYuj))
        z = np.dot(p,(u1.transpose() + WYuj)
    
        #W[:,0:1] = z.reshape(4,1)
        aux = W.transpose()
        aux[::][-1] = z
        W = aux.transpose()
        #Y[:,0:1] = u1.reshape(4,1)
        aux = Y.transpose()
        aux[::][-1] = u1
        Y = aux.transpose()
     
    Q = np.indentity(4) + np.dot(W, np.matrix.conjugate(Y))
    return Q
""
#T = np.array([1,0,0],[1,1,0],[1,1,1],[1,1,1])
#ProdHi(T)

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

def factR(A):
    (num_rows, num_cols) = np.shape(A)    
    
    T = np.empty([num_rows,num_cols])
    
    for cont in range(len(A[0]-1)):
        x = np.array([A[cont:, cont]]).transpose()
        e1 = np.eye(len(x),1)
        u = x + np.sign(x[0][0])*np.linalg.norm(x)*e1
        #pprint(u)
    
        x1 = MatVecHH(x,u)
        if(len(x1) != num_rows):
            N = num_rows - len(x1)
            for i in range(N):
                p = np.zeros(1)
                x1 = np.append(x1,p)
            x1 = np.reshape(x1,(num_cols,1))
            x1 = x1[::-1]
        
        T[:,cont:cont+1] = x1
    return T
    
def factQR(A):
    T = factR(A)
    #pprint(T)
    Q = ProdHi(T)
    R = np.dot(Q.transpose(), A)
    return Q, R    


A = np.array([[-2,5,7,4],
              [7,1,-10,1],
              [4,8,-4,9],
              [3,12,1,8]],dtype = 'float64')
    
Q, R = factQR(A)
pprint(Q)
pprint(R)
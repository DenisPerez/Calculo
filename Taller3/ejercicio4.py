# -*- coding: utf-8 -*-

import scipy.linalg as sla
from math import sqrt
from pprint import pprint


def cholesky(A):
    n = len(A)
    
    L = [[0.0]* n for i in range(n)]
    
    
    for i in range(n):
        for k in range(i+1):
            
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i==k):
                #LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                #LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L


A = [[6,3,4,8], [3,6,5,1], [4,5,10,7], [8,1,7,25]]

L = cholesky(A)


print ("A:")
pprint(A)
print("L:")
pprint(L)

L = sla.cholesky(A)
pprint(L)
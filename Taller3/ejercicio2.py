import numpy as np
from pprint import pprint

def y(a,b,c):
    n = len(a)
    arr = [None]*n
    arr[0] = a[0]
    for i in range(1,n):
        arr[i] = a[i] - c[i-1]*b[i-1]/arr[i-1]
    return arr

def tridiag(beta,b,c):
    n = len(beta)
    L = np.identity(n)
    U = np.identity(n)
    for i in range (n-1):
        L[i+1][i] = c[i]/beta[i]
        U[i][i] = beta[i]
        U[i][i+1] = b[i]
    U[n-1][n-1] = beta[n-1]
    return L, U
    
a = [1,2,3,4]
b = [2,2,2,2]
c = [3,3,3,3]

#m = 5
#a = [1 for i in range(m)]
#b = [2 for i in range(m)]
#c = [2 for i in range(m)]

L, U = tridiag(y(a,b,c), b, c)
pprint(L)
print()
pprint(U)
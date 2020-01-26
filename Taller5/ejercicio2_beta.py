import random
import numpy as np
import scipy.linalg as sla
from pprint import pprint

y = lambda i, flag: 1.00005 if flag == True and i == 0 else 1

def Kinf(A):
    if( max(A[:,0]) == 1 ):
        return 1
    else:
        return max(A[:,0])

def matrixA(n,m):
    A = np.identity(n)
    for i in range(1,n):
        A[i][0] = random.uniform(0,m)
        
    return A

n = 5


#Case ai = 0.01

A = matrixA(n, 0.01); cond = Kinf(A)

b = [y(i, False) for i in range(n)]
x = sla.solve(A, b)

b_ = [y(i, True) for i in range(n)]
x_ = sla.solve(A, b_)

print("Caso ai = 0.01:")
print(cond)
pprint(x)
pprint(x_)

#Case ai = 100

A = matrixA(n, 100); cond = Kinf(A)

b = [y(i, False) for i in range(n)]
x = sla.solve(A, b)

b_ = [y(i, True) for i in range(n)]
x_ = sla.solve(A, b_)

print("\nCaso ai = 100:")
print(cond)
pprint(x)
pprint(x_)

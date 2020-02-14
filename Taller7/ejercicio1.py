import numpy as np
import scipy.linalg as sla
from pprint import pprint

def createA(e):
    A = np.zeros((4,3))
    A[0] = [1,1,1]
    A[1:4] = e*np.identity(3)
    return A

def createAtA(e):
    A = np.ones((3,3))
    A = A + (e**2)*np.identity(3)
    return A

def createb(e):
    b = np.ones((4,1))
    b[0] = 3
    b[1:4] = [e, e, e]
    return b

def createAtb(e):
    b = np.ones((3,1))
    b = (3+(e**2))*b
    return b

def xCholesky(e):
    L = np.zeros((3,3))
    a = (1+(e**2))**(1/2)
    L[0][0] = a
    L[1][0] = 1/a
    L[1][1] = 1+(e**2)
    L[2][0] = L[1][0]
    L[2][1] = 1
    L[2][2] = L[1][1]
    x = sla.solve(L@L.T, createAtb(e))
    return x

def xHouseholder(e):
    
    
    
    
    return x

def xGramSchmidt(e):
    
    
    
    
    return x
    
results = np.zeros((5,7))
x_star = np.ones((3,1))

#Case e = 10^0

e = 1

A = createA(e)
b = createb(e)
xc = xCholesky(e)
xh = xHouseholder(e)
xg = xGramSchmidt(e)

cond = np.linalg.cond(A, p='fro')
rc = np.linalg.norm(b - A@xc, 2)
ec = np.linalg.norm(x_star - xc, 2)
rh = np.linalg.norm(b - A@xh, 2)
eh = np.linalg.norm(x_star - xh, 2)
rg = np.linalg.norm(b - A@xg, 2)
eg = np.linalg.norm(x_star - xg, 2)
results[0][0] = cond
results[0][1] = rc
results[0][2] = rh
results[0][3] = rg
results[0][4] = ec
results[0][5] = eh
results[0][6] = eg

#Case e = 10^-2

e = 10**(-2)

A = createA(e)
b = createb(e)
xc = xCholesky(e)
xh = xHouseholder(e)
xg = xGramSchmidt(e)

cond = np.linalg.cond(A, p='fro')
rc = np.linalg.norm(b - A@xc, 2)
ec = np.linalg.norm(x_star - xc, 2)
rh = np.linalg.norm(b - A@xh, 2)
eh = np.linalg.norm(x_star - xh, 2)
rg = np.linalg.norm(b - A@xg, 2)
eg = np.linalg.norm(x_star - xg, 2)
results[1][0] = cond
results[1][1] = rc
results[1][2] = rh
results[1][3] = rg
results[1][4] = ec
results[1][5] = eh
results[1][6] = eg

#Case e = 10^-4

e = 10**(-4)

A = createA(e)
b = createb(e)
xc = xCholesky(e)
xh = xHouseholder(e)
xg = xGramSchmidt(e)

cond = np.linalg.cond(A, p='fro')
rc = np.linalg.norm(b - A@xc, 2)
ec = np.linalg.norm(x_star - xc, 2)
rh = np.linalg.norm(b - A@xh, 2)
eh = np.linalg.norm(x_star - xh, 2)
rg = np.linalg.norm(b - A@xg, 2)
eg = np.linalg.norm(x_star - xg, 2)
results[2][0] = cond
results[2][1] = rc
results[2][2] = rh
results[2][3] = rg
results[2][4] = ec
results[2][5] = eh
results[2][6] = eg

#Case e = 10^-8

e = 10**(-8)

A = createA(e)
b = createb(e)
xc = xCholesky(e)
xh = xHouseholder(e)
xg = xGramSchmidt(e)

cond = np.linalg.cond(A, p='fro')
rc = np.linalg.norm(b - A@xc, 2)
ec = np.linalg.norm(x_star - xc, 2)
rh = np.linalg.norm(b - A@xh, 2)
eh = np.linalg.norm(x_star - xh, 2)
rg = np.linalg.norm(b - A@xg, 2)
eg = np.linalg.norm(x_star - xg, 2)
results[3][0] = cond
results[3][1] = rc
results[3][2] = rh
results[3][3] = rg
results[3][4] = ec
results[3][5] = eh
results[3][6] = eg

#Case e = 10^-10

e = 10**(-10)

A = createA(e)
b = createb(e)
xc = xCholesky(e)
xh = xHouseholder(e)
xg = xGramSchmidt(e)

cond = np.linalg.cond(A, p='fro')
rc = np.linalg.norm(b - A@xc, 2)
ec = np.linalg.norm(x_star - xc, 2)
rh = np.linalg.norm(b - A@xh, 2)
eh = np.linalg.norm(x_star - xh, 2)
rg = np.linalg.norm(b - A@xg, 2)
eg = np.linalg.norm(x_star - xg, 2)
results[4][0] = cond
results[4][1] = rc
results[4][2] = rh
results[4][3] = rg
results[4][4] = ec
results[4][5] = eh
results[4][6] = eg

pprint(results)
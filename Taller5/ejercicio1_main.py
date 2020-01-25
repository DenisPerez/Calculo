import numpy as np
import scipy.linalg as sla
from B_ejercicio1 import B
from tabla_ejercicio1 import table

A = np.random.rand(5,5)
Q, R = np.linalg.qr(A)
I = np.identity(5)
Be = B(A, I, Q, R)
K_fro = np.linalg.cond(A, p = 'fro')
Norm_froB = np.linalg.cond( (I - np.dot(A,Be)), p = 'fro')
A_inv = sla.inv(A)
Norm_fro = np.linalg.cond( (I - np.dot(A,A_inv)), p = 'fro')

results = np.zeros((4,3))
results[0][0] = K_fro
results[0][1] = Norm_froB
results[0][2] = Norm_fro

A = sla.hilbert(5)
K_fro = np.linalg.cond(A, p = 'fro')
Q, R = np.linalg.qr(A)
Be = B(A, I, Q, R)
Norm_froB = np.linalg.cond( (I - np.dot(A, Be)), p = 'fro')
A_inv = sla.invhilbert(5)
Norm_fro = np.linalg.cond( (I - np.dot(A,A_inv)), p = 'fro')

results[1][0] = K_fro
results[1][1] = Norm_froB
results[1][2] = Norm_fro

I = np.identity(20)
A = np.random.rand(20,20)
K_fro = np.linalg.cond(A, p = 'fro')
Q, R = np.linalg.qr(A)
Be = B(A, I, Q, R)
Norm_froB = np.linalg.cond( (I - np.dot(A, Be)), p = 'fro')
A_inv = sla.inv(A)
Norm_fro = np.linalg.cond( (I - np.dot(A, A_inv)), p = 'fro')

results[2][0] = K_fro
results[2][1] = Norm_froB
results[2][2] = Norm_fro

A = sla.hilbert(20)
K_fro = np.linalg.cond(A, p = 'fro')
A_inv = sla.invhilbert(20)
Q, R = np.linalg.qr(A)
Be = B(A, I, Q, R)
Norm_froB = np.linalg.cond( (I - np.dot(A, Be)), p = 'fro')
Norm_fro = np.linalg.cond( (I - np.dot(A, A_inv)), p = 'fro')

results[3][0] = K_fro
results[3][1] = Norm_froB
results[3][2] = Norm_fro

table(results)

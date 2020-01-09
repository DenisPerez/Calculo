# -*- coding: utf-8 -*-
from pprint import pprint # pretty print import
import scipy as sp
import scipy.linalg as sla
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file = "/home/denis/Downloads/Ellapiz.jpg"

Ag = mpimg.imread(file)
dim = Ag.shape
A = Ag.reshape((dim[0],dim[1]*3))
U,S,V = sla.svd(A,full_matrices = False)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.imshow(A)
ax.axis('off')

#pprint(A) Matrix A

rango = np.linalg.matrix_rank(A)
n = 20
Ak = np.zeros((len(U), len(V.T)))
for k in range(n):
    #Ak = Ak + S[k]*np.dot(U[k].reshape(dim[0], 1), V[:, k].reshape(1,dim[0]))
    Ak += S[k] * np.outer(U.T[k], V[k])

#pprint(Ak) Matrix Ak

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
"""
#Descomentar la siguiente linea si lo que se quiere es reconstruir la
imagen a color comprimida
ax.imshow((Ak.reshape(dim[0],dim[1],3)).astype('uint8'))
"""
ax.imshow(Ak)
ax.axis('off')


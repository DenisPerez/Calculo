# -*- coding: utf-8 -*-

import scipy.linalg as sla
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file = "Ellapiz.jpg"

Ag = mpimg.imread(file)
dim = Ag.shape
A = Ag.reshape((dim[0],dim[1]*3))
U,S,V = sla.svd(A,full_matrices = False)
"""
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.imshow(A)
ax.axis('off')
"""


rango = np.linalg.matrix_rank(A)
n = 20
Ak = np.zeros((len(U), len(V.T)))
for k in range(n):

    Ak += S[k] * np.outer(U.T[k], V[k])

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Descomentar la siguiente linea si lo que se quiere es reconstruir la
#imagen a color comprimida
ax.imshow((Ak.reshape(dim[0],dim[1],3)).astype('uint8'))

#ax.imshow(Ak)
ax.axis('off')


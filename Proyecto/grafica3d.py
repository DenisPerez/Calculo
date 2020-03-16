# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:42:16 2020

@author: Usuario
"""

import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pl

p1 = 1000
p2 = 2000
h1 = 5
s = 10

C = lambda x, h2 : (p1*h1/np.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.sqrt(h2**2+(s-x)**2)**3)

fig = pl.figure()
ax = fig.gca(projection='3d')
x = np.arange(0, s, 0.1)
h2 = np.arange(3, 10, 0.1)
x, h2 = np.meshgrid(x, h2)
z = (p1*h1/np.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.sqrt(h2**2+(s-x)**2)**3)

ax.plot_surface(x, h2, z, rstride=1, cstride=1, cmap=pl.cm.coolwarm)
ax.contourf(x, h2, z, zdir='z', offset=-2, cmap=pl.cm.coolwarm)

pl.show()

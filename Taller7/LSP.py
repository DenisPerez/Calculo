# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp
from recta_lsp import rectaLSP
from parabola2_lsp import parabola2LSP
from parabola1_lsp import parabola1LSP
from parabola_lsp import parabolaLSP
import matplotlib.pyplot as plt

x = [0,1,2,3]
y = [4,5,8,1]

x_recta, r_recta = rectaLSP(x,y)
x_parabola2, r_parabola2 = parabola2LSP(x,y)
x_parabola1, r_parabola1 = parabola1LSP(x,y)
x_parabola, r_parabola = parabolaLSP(x,y)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

x1 = np.linspace(-0.6,3.6,4)
plt.scatter(0,4)
plt.scatter(1,5)
plt.scatter(2,8)
plt.scatter(3,1)
plt.title("Aproximaciones de diferentes funciones usando LSP",pad = 50, fontsize = 'medium')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x1,x_recta[0]*x + x_recta[1], '--r', label = '$y = mx + d$')
plt.plot(x1,x_parabola[0]*[x**2 for x in range(4)] + x_parabola[1], '-.g', label = '$y = m x^2 + d$')
plt.plot(x1,x_parabola2[0]*[x**2 for x in range(4)] + x_parabola2[1]*x + x_parabola2[2], ':b', label = '$y = mx^2+ zx + d$')
plt.plot(x1,x_parabola1[0]*[x**2 for x in range(4)] + x_parabola1[1]*x, '--m', label = '$y = mx^2+ zx$')
plt.legend(loc = 'lower right', fontsize = 'x-small')

plt.show()

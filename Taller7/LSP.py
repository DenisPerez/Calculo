# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp
from recta_lsp import rectaLSP
import matplotlib.pyplot as plt

x = [0,1,2,3]
y = [4,5,8,1]

x_recta = rectaLSP(x,y)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

x1 = np.linspace(-0.6,3.6,4)
plt.scatter(0,4)
plt.scatter(1,5)
plt.scatter(2,8)
plt.scatter(3,1)

plt.plot(x1,x_recta[0]*x + x_recta[1], '--r', label = 'y = mx + d')

#plt.legend(loc = 'upper right')

plt.show()

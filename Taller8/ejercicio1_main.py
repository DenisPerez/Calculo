# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

eq_spaced =  np.arange(-1,1,0.068)


minus_simetric = np.random.uniform(low = -1.0, high = 0.0, size = 15)
simetric_spaced = np.concatenate([minus_simetric, -minus_simetric])

r1 = 0.75 * np.random.uniform(low = 0, high = 1.0, size = 5)
r2 = 1 + (0.75-1) * np.random.uniform(low = 0, high = 1.0 , size = 10)
nra1 = np.concatenate([r1,r2])
smart_spaced = np.concatenate([-nra1, nra1])

plt.figure()

##equaly spaced nodes

y = abs(eq_spaced)

f1 = lagrange(eq_spaced, y)

xx1 = np.linspace(min(eq_spaced), max(eq_spaced), num = 100)

plt.subplot(221)
plt.plot(xx1,f1(xx1), 'r')
plt.grid(True)

values = np.arange(-1,1,0.1)

e = abs(values) - f1(values)

#simetric spaced nodes

y2 = abs(simetric_spaced)

f2 = interp1d(simetric_spaced, y2, kind = 'quadratic', fill_value = 'extrapolate')

xx2 = np.linspace(min(simetric_spaced), max(simetric_spaced))

plt.subplot(222)
plt.plot(xx2,f2(xx2),'b')
plt.grid(True)

values = np.arange(-1,1,0.1)

e1 = abs(values) - f2(values)

## smart_spaced

y3 = abs(smart_spaced)

f3 = interp1d(smart_spaced, y3, kind = 'quadratic', fill_value = 'extrapolate')

xx3 = np.linspace(min(smart_spaced), max(smart_spaced))

plt.subplot(223)
plt.plot(xx3,f3(xx3),'g')
plt.grid(True)

values = np.arange(-1,1,0.1)

e2 = abs(values) - f3(values)

plt.subplot(224)
plt.plot(values,e,'r')
plt.plot(values,e1,'b')
plt.plot(values,e2,'g')
plt.grid(True)
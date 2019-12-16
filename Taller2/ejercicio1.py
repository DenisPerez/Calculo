# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import scipy as s


def f(x, n): return (x**n)/(x+5)


def generateFunction(n):
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.grid()
    xtricks = s.linspace(0, 1, 110)
    function = []

    for x in np.arange(0, 1.1, 0.01):
        function.append(f(x, n))
    ax1.plot(xtricks, function, label='$f(x)$')
    ax1.legend(loc=0)


for i in range(5, 25, 5):
    generateFunction(i)

for i in range(30, 70, 10):
    generateFunction(i)

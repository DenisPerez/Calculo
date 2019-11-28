# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
#import numpy as np
import scipy as s
import random


w = s.linspace(0,1,50)
n = 1000

xvalues = []
yvalues = []

def transformacion(n):
    for i in range(n):
        r = random.uniform(0,1)
        if(r < 0.85):
            xvalues.append(0.445) # A1x + b1
            yvalues.append(2.005)
        elif(r < 0.92):
            xvalues.append(-0.03) # A2x + b2
            yvalues.append(0.665)
        elif(r < 0.99):
            xvalues.append(0.065) # A3x + b3
            yvalues.append(0.665)
        elif(r <= 1):
            xvalues.append(0)     # A4x
            yvalues.append(0.08)

transformacion(n)
plt.scatter(xvalues,yvalues)
plt.scatter([0.5],[0.5])
plt.show()

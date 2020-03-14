# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
from root import bisection
from root import intersection
#Constant values
h1 = 5
h2 = 6
p1 = 1000
p2 = 2000
s = 10

C = lambda h1,h2,p1,p2,s,x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)
f1 = lambda h1,h2,p1,p2,s,x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3))
f2 = lambda h1,h2,p1,p2,s,x : (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)
derC = lambda h1,h2,p1,p2,s,x : -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

#Distantce in X
x = np.arange(0,11,1) 

#Y values
y1 = [f1(h1,h2,p1,p2,s,i) for i in x]
y2 = [f2(h1,h2,p1,p2,s,i) for i in x]
c = [C(h1,h2,p1,p2,s,i) for i in x]
dc = [derC(h1,h2,p1,p2,s,i) for i in x]

#plot functions
plt.plot(x,y1,'o-')
plt.plot(x,y2,'--')
plt.plot(x,c,'--o')
plt.plot(x,dc,'*-')

x_eq_aprox = ((10-0)/2.0) + 0.5
x_max_aprox = (10)
x_min_aprox = (10-0)/2.0

x_min = bisection(x_min_aprox-0.5, x_min_aprox+0.5, 1e-15)
x_max = bisection(x_max_aprox-0.5, x_max_aprox, 1e-15)
x_eq = intersection(x_eq_aprox-0.5, x_eq_aprox+0.5, 1e-15)
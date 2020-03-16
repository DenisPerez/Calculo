# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
import random as rand
from random import random
from find_intervals import intervals
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import sys



h1 =5
p1 = 1000
p2 = 2000
s = 30
hh2 = np.linspace(3.0,10.0,num=30)
ra1 = rand.uniform(0,1)
ra2 = rand.uniform(s-1,s)

C = lambda x,h2 : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

derC = lambda x,h2 : -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

x = np.linspace(0,s,num = 30)

def L1 (x):
    return (p1*h1/np.sqrt((h1**2 + x**2)**3))

def L2(x,h2):
    return (p2*h2/np.sqrt(h2**2+(s-x)**2)**3)

def Cx (x,h2):
    return L1(x) + L2(x,h2)

def derCx(x,h2):
    return -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

#def matrixC(X,Y):
    

def bisection(a,b, tol,h2):
    
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        
        c = (xl+xr)/2.0
        prod = derCx(xl,h2) * derCx(c,h2)
        
        if prod > tol:
            xl = c
            
        else:
            if prod < tol:
                xr = c
        
    return c


def minimun_interval(intervalos_aprox,h2):
    intervalos = []

    for i in range (len(intervalos_aprox)):
        xl = intervalos_aprox[i][0]
        xr = intervalos_aprox[i][1]

        
        cl = derCx(xl,h2)
        cr = derCx(xr+1,h2)
        
        if cl < 0 and cr > 0 :
            print("Minimun at", intervalos_aprox[i])
            intervalos.append(intervalos_aprox[i])
    return (intervalos)

x_min_array = []

for i in range (len(hh2)):
    dc1 = []
    for j in range(len(x)):
        dc1.append(derC(x[j],hh2[i]))
    intervalos_aproximados = intervals(dc1)

    minimun_intervalos = minimun_interval(intervalos_aproximados,hh2[i])

    if (len(minimun_intervalos) != 0 ):
        x_min_temp = bisection(minimun_intervalos[0][0],minimun_intervalos[0][1], 1e-20, hh2[i])
        x_min_array.append(x_min_temp)
    else:
        if C(rand.uniform(0,1),hh2[i]) > C(rand.uniform(s-2,s),hh2[i]) :
            x_min_array.append(s)
        else:
            x_min_array.append(0 + rand.uniform(0,1))
            
C2 = lambda x, h2 : (p1*h1/np.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.sqrt(h2**2+(s-x)**2)**3)



fig = plt.figure()
ax = fig.gca(projection='3d')
plt.plot(x_min_array, hh2, Cx(x, hh2), marker='*', linestyle='')
x = np.arange(0, s, 0.1)

h2 = np.arange(3, 10, 0.1)

#x, hh2 = np.meshgrid(x, hh2)
#ax.plot_surface(x, hh2, C2(x, hh2), rstride=1, cstride=1, cmap=plt.cm.coolwarm)
#ax.contour(x, hh2, C2(x, hh2), zdir='z', offset=0, cmap=plt.cm.coolwarm)

x, h2 = np.meshgrid(x, h2)
z = C2(x,h2)
ax.plot_surface(x, h2, z, rstride=1, cstride=1, cmap=plt.cm.coolwarm)
ax.contour(x, h2, z, zdir='z', offset=0, cmap=plt.cm.coolwarm)

plt.show()
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
s = 10
hh2 = np.arange(3,10.1,0.7)
ra1 = rand.uniform(0,1)
ra2 = rand.uniform(s-1,s)

C = lambda x,h2 : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

derC = lambda x,h2 : -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

x = np.arange(0,11,1)

def L1 (x):
    return (p1*h1/np.math.sqrt((h1**2 + x**2)**3))

def L2(x,h2):
    return (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

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
        mid_point = (xr+xl)/2
        
        cl = derCx(mid_point-2,h2)
        cr = derCx(mid_point+2,h2)
        
        if cl < 0 and cr > 0 :
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
        x_min_array.append(bisection(minimun_intervalos[0][0],minimun_intervalos[0][1], 1e-20, hh2[i]))
    else:
        if C(rand.uniform(0,1),hh2[i]) > C(rand.uniform(s-2,s),hh2[i]) :
            x_min_array.append(s)
        else:
            x_min_array.append(0 + rand.uniform(0,1))
c = []
for h in hh2:
    for xs in x:
      c.append(Cx(xs,h))
      
      
plt.plot(hh2,x_min_array,'-o')
fig = plt.figure()
ax = fig.gca(projection = '3d')

X = np.arange(-2,2,0.1)
Y = np.arange(-2,2,0.1)

X,Y = np.meshgrid(X,Y)

#R = Cx(X,Y)


        
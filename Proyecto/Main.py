# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
import random as rand
from random import random
from find_intervals import intervals

upper_limit = 10.0
lower_limit = 3.0

upper_limit1 = 1000
lower_limit1 = 2000

upper_limit2 = 0
lower_limit2 = 30

h1 = random() * (upper_limit - lower_limit) + lower_limit
h2 = random() * (upper_limit - lower_limit) + lower_limit
p1 = random() * (upper_limit1 - lower_limit1) + lower_limit1
p2 = random() * (upper_limit1 - lower_limit1) + lower_limit1
#s = random() * (upper_limit2 - lower_limit2) + lower_limit2
s = 14

#function zone
def L1 (x):
    return (p1*h1/np.math.sqrt((h1**2 + x**2)**3))

def L2(x):
    return (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

def Cx (x):
    return -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

def bisection(a,b, tol):
    
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        
        c = (xl+xr)/2.0
        prod = Cx(xl) * Cx(c)
        
        if prod > tol:
            xl = c
            
        else:
            if prod < tol:
                xr = c
        
    return c


def intersection(a,b, tol):
    
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        
        c = (xl+xr)/2.0
        minus = L1(xl) - L2(c)
        
        if minus > tol:
            xl = c
            
        else:
            if minus < tol:
                xr = c
        
    return c

###code zone


#lambda functions

C = lambda x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)
f1 = lambda x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3))
f2 = lambda x : (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)
derC = lambda x : -((3*p1*h1*x*(x**2+h1**2)**2)/((h1**2+x**2)**3)**(3/2)) + ( (3*h2*p2*((-x+s)**2 + h2**2)**2 * (-x+s)) / ((h2**2 + (s-x)**2)**3)**(3/2))

#Distantce in X
x = np.arange(0,15,1)

#Y values
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
c = [C(i) for i in x]
dc = [derC(i) for i in x]

#plot functions
plt.plot(x,y1,'o-')
plt.plot(x,y2,'--')
plt.plot(x,c,'--o')
plt.plot(x,dc,'*-')

#set intervals 
intervalos_aprox = intervals(dc)
maximun_point = []
minimum_point = []
intervalos = []
values = []

#Esta funcion diferencia entre maximos y minimos
#Luego separa solo los intervalos de interes
for i in range (len(intervalos_aprox)):
    xl = intervalos_aprox[i][0]
    xr = intervalos_aprox[i][1]
    mid_point = (xr+xl)/2
    
    cl = Cx(mid_point-0.5)
    cr = Cx(mid_point+1)
    
    if cl < 0 and cr > 0 :
        minimum_point.append(mid_point)
        intervalos.append(intervalos_aprox[i])
        
    else:
        if cl > 0 and cr < 0:
            maximun_point.append(mid_point)
            if len(maximun_point) > 1:
                    c = C(maximun_point[0])
                    c1 = C(maximun_point[1])
                    if c > c1:
                        x_max_aprox = maximun_point[0]
                    else:
                        x_max_aprox = maximun_point[1]
                        values.pop()
                        values.append(intervalos_aprox[i])
            else:
                values.append(intervalos_aprox[i])

#set aprox values
intervalos.append(values[0])
x_min_aprox = min(minimum_point)

#@comprobamos si hay interseccion
intersectionFlag = False
if ((f2(0) >= f1(0) and f2(s) <= f1(s)) or (f1(0) >= f2(0) and f1(s) <= f2(s))):
    intersectionFlag = True
    
#si hay interseccion
if intersectionFlag:
    x_eq_aprox = x_min_aprox + rand.choice([-1,1])
    x_eq = intersection(0, s, 1e-15)

#bisection en los intervalos de interes
x_min = bisection(intervalos[0][0], intervalos[0][1], 1e-15)
x_max = bisection(intervalos[1][0], intervalos[1][1], 1e-15)



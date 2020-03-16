# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
import random as rand
from random import random
from find_intervals import intervals
import math

upper_limit = 10.0
lower_limit = 3.0

upper_limit1 = 1000
lower_limit1 = 2000

upper_limit2 = 0
lower_limit2 = 30


h1 = 5
h2 = 10
p1 = 1000
p2 = 2000
s = 30
#h1 = random() * (upper_limit - lower_limit) + lower_limit
#h2 = random() * (upper_limit - lower_limit) + lower_limit
#p1 = random() * (upper_limit1 - lower_limit1) + lower_limit1
#p2 = random() * (upper_limit1 - lower_limit1) + lower_limit1
#s = random() * (upper_limit2 - lower_limit2) + lower_limit2

#function zone
def L1 (x):
    return (p1*h1/np.sqrt((h1**2 + x**2)**3))

def L2(x):
    return (p2*h2/np.sqrt(h2**2+(s-x)**2)**3)

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
        
        c = (xr+xl)/2.0
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
derC = lambda x : ((3*h2*p2*(s-x))/((s-x)**2+h2**2)**5/2) - ((3*h1*p1*x))/(x**2+h1**2)**5/2

#Distantce in X
#x = np.arange(0,math.ceil(s)+1,1)
x = np.linspace(0,s,num = s)
#Y values
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
c = [C(i) for i in x]
dc = [derC(i) for i in x]

plt.rcParams.update({'figure.figsize': [6,5],'font.size': 18, 'font.family': 'serif'})


fig = plt.figure()
ax1 =  fig.add_axes([0.1,0.1,0.8,0.8])
ax1.grid()
ax1.plot(c,'g-o',label='$C(x)$')
ax1.plot(y1,'bo--',label='$L_{1}(x)$')
ax1.plot(y2,'y--*',label='$L_{2}(x)$')
#ax1.plot(dc,'r-*',label='$C(x)$')
ax1.set_xlabel('')
ax1.set_ylabel('Vatios')
ax1.legend(loc=0)

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
    
    cl = Cx(mid_point-2)
    cr = Cx(mid_point+2)
    
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
if (len(intervalos) == 1):
    x_max = bisection(intervalos[0][0], intervalos[0][1], 1e-20)
    if C(rand.uniform(0,1)) > C(rand.uniform(s-2,s)) :
        x_min_approx = s - rand.uniform(0,1)
        x_min = s
    else:
        x_min_approx = 0 + rand.uniform(0,1)
        x_min = 0 + rand.uniform(0,1)
else:
    #bisection en los intervalos de interes
    x_min_approx = min(minimum_point)
    x_min = bisection(intervalos[0][0], intervalos[0][1], 1e-20)
    x_max = bisection(intervalos[1][0], intervalos[1][1], 1e-20)
    ra = rand.uniform(0,1)
    rt = C(x_min)
    if (C(ra) < rt):
        x_min = ra
    else:
        if (C(s) < rt):
            x_min = s
    
#@comprobamos si hay interseccion
intersectionFlag = False
if ((f2(0) >= f1(0) and f2(s) <= f1(s)) or (f1(0) >= f2(0) and f1(s) <= f2(s))):
    intersectionFlag = True
    
#si hay interseccion
if intersectionFlag:
    x_eq_aprox = x_min_approx + rand.uniform(-1,1)
    x_eq = intersection(0, math.ceil(s/2), 1e-20)

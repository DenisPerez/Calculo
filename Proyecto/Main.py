# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import optimize

C = lambda h1,h2,p1,p2,s,x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)
f1 = lambda h1,h2,p1,p2,s,x : (p1*h1/np.math.sqrt((h1**2 + x**2)**3))
f2 = lambda h1,h2,p1,p2,s,x : (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

#Constant values
h1 = 5
h2 = 6
p1 = 1000
p2 = 2000
s = 10

#Distantce in X
x = np.arange(-30,11,1) 

#Y values
y1 = [f1(h1,h2,p1,p2,s,i) for i in x]
y2 = [f2(h1,h2,p1,p2,s,i) for i in x]
c = [C(h1,h2,p1,p2,s,i) for i in x]

#plot functions
plt.plot(x,y1,'-')
plt.plot(x,y2,'-')
plt.plot(x,c,'-')





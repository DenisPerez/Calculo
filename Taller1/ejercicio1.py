# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:22:25 2019

@author: Usuario
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import scipy as s

r = 1/2
n = 30
unitcircle = plt.Circle((0,0),r,color='b',fill=False)

plt.rcParams.update({'figure.figsize': [8,6],'font.size': 18, 'font.family': 'serif'})

fig = plt.figure()
ax = plt.subplot(aspect='equal')
ax.add_artist(unitcircle)
temp = s.linspace(-0.6,0.6)
line, = ax.plot(temp, temp, lw=2)

pi_aproximations = []

def init():
    line.set_data([], [])
    return line,

def animate(i):
    coseno = lambda i,k : r * (s.cos(((2*np.pi)*(k))/i))
    seno = lambda i,k : r * (s.sin(((2*np.pi)*(k))/i))
    xvalues = []
    yvalues = []
    
    for j in range(i+5):
        xvalues.append(coseno(i+4,j))
        yvalues.append(seno(i+4,j))
    line.set_color('purple')
    line.set_data(xvalues, yvalues)
    
    return line,

def polygon(n):
    
    coseno = lambda n,k : r * (s.cos(((2*np.pi)*(k))/n))
    seno = lambda n,k : r * (s.sin(((2*np.pi)*(k))/n))
    xvalues = []
    yvalues = []

    for i in range(n+1):
        xvalues.append(coseno(n,i))
        yvalues.append(seno(n,i))
        #ax.plot(xvalues,yvalues, 'r')
        
    
    x = (xvalues[1]-xvalues[0])**2
    y = (yvalues[1] - yvalues[0])**2
        
    L = 0
    L = (n)*np.sqrt(x + y)
    pi_aproximations.append(L)

for i in range(4,n+1):
    polygon(i)
result = list(map(lambda y: np.abs(np.pi-y), pi_aproximations))

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = n, interval = 150, blit = True)

anim.save('polygon30.gif', writer='imagemagick')

xticks = s.linspace(4,n,n-3)

fig1, ax1 = plt.subplots(figsize = (6,4))
ax1.semilogy(xticks, result, 'r', label='$|\pi - L_{n}|$ escala $log_{10}$') if (n > 15) else ax1.plot(xticks, result, 'r', label='$|\pi - L_{n}|$ escala lineal')
ax1.set_title('$Error\quad de\quad aproximación\quad de\quad\pi$')
ax1.set_xlabel('$ \#\quadde\quad lados \quad del \quad poligono$')
ax1.set_ylabel('Tamaño del $Error$')

ax1.legend(loc=0)

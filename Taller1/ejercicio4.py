# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
#import numpy as np
import scipy as s
import random
import numpy as np

A1 = np.array([[0.85,0.04],[-0.04,0.85]])
A2 = np.array([[0.20,-0.26],[0.23,0.22]])
A3 = np.array([[-0.15,0.28],[0.26,0.24]])
A4 = np.array([[0,0],[0,0.16]])
b1 = np.array([[0],[1.6]])
b = np.array([[0],[0.44]])

x = np.array([[0.5],[0.5]])


#w = s.linspace(0,1,50)
n = 300000

xvalues = []
yvalues = []

def transformacion(n):
    x = np.array([[0.5],[0.5]])
    for i in range(n):
        r = random.uniform(0,1)
        if(r < 0.85):
            temp = np.add(np.dot(A1,x),b1)
            xvalues.append(temp[0]) # A1x + b1
            yvalues.append(temp[1])
            x = temp

        elif(r < 0.92):
            temp = np.add(np.dot(A2,x),b)
            xvalues.append(temp[0]) # A1x + b1
            yvalues.append(temp[1])
            x = temp

        elif(r < 0.99):
            temp = np.add(np.dot(A3,x),b)
            xvalues.append(temp[0]) # A1x + b1
            yvalues.append(temp[1])
            x = temp

        elif(r <= 1):
            temp = np.dot(A4,x)
            xvalues.append(temp[0]) # A1x + b1
            yvalues.append(temp[1])
            x = temp

transformacion(n)
plt.scatter(xvalues,yvalues,color = "green")
plt.show()

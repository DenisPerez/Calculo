# -*- coding: utf-8 -*-

from pprint import pprint # pretty print import
import numpy as np # numyp import
from numpy import finfo # Epsilon import
from numpy import eye #Eye function import
from numpy import sqrt #Square root import
from numpy.random import randn #random library

x1 = eye(6,1)+100*sqrt(finfo(float).eps)*randn(6,1)
x2 = -x1
x3 = eye(6,1)+sqrt(finfo(float).eps)+randn(6,1)
x4 = -x3
x5 = eye(6,1)+(sqrt(finfo(float).eps)/100)*randn(6,1)
x6 = -x5
x7 = eye(6,1)+(sqrt(finfo(float).eps)/1000)*randn(6,1)
x8 = -x7
e1 = eye(1,6)

pprint(x1.transpose())
print(x1[0][0])
pprint(finfo(float).eps)

"""
Prints para cada uno de los arrays
pprint(x1)
pprint(x2)
pprint(x3)
pprint(x4)
pprint(x5)
pprint(x6)
pprint(x7)
pprint(x8)
"""

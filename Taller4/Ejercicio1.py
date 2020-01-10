# -*- coding: utf-8 -*-

from texttable import Texttable

from pprint import pprint # pretty print import
import numpy as np # numyp import
from numpy import finfo # Epsilon import
from numpy import eye #Eye function import
from numpy import sqrt #Square root import
from numpy.random import randn #random library
from PositiveHouseHolder import PositiveHouseHolder as PH
from NegativeHouseHolder import NegativeHouseHolder as NH

x1 = eye(6,1)+100*sqrt(finfo(float).eps)*randn(6,1)
x2 = -x1
x3 = eye(6,1)+sqrt(finfo(float).eps)+randn(6,1)
x4 = -x3
x5 = eye(6,1)+(sqrt(finfo(float).eps)/100)*randn(6,1)
x6 = -x5
x7 = eye(6,1)+(sqrt(finfo(float).eps)/1000)*randn(6,1)
x8 = -x7
e1 = eye(6,1)



np.linalg.norm(np.dot(PH(x1,e1),))


"""
t = Texttable() # create the table to put the data inside
t.add_rows([['xi',
             'signo(xi)',
             '||PHi xi - alphai e1||2',
             '||I - PHi.T PHi||2',
             '||NHi xi + alphai e1||2', 
             '||I - NHi.T NH||2']])

#draw the table t
print(t.draw())

"""

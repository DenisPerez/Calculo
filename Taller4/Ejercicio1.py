# -*- coding: utf-8 -*-

from texttable import Texttable

import numpy as np # numyp import
from numpy import finfo # Epsilon import
from numpy import eye #Eye function import
from numpy import sqrt #Square root import
from numpy.random import randn #random library
from PositiveHouseHolder import PositiveHouseHolder as PH
from NegativeHouseHolder import NegativeHouseHolder as NH

I = np.identity(6)

x1 = eye(6,1)+100*sqrt(finfo(float).eps)*randn(6,1)
x2 = -x1
x3 = eye(6,1)+sqrt(finfo(float).eps)+randn(6,1)
x4 = -x3
x5 = eye(6,1)+(sqrt(finfo(float).eps)/100)*randn(6,1)
x6 = -x5, P
x7 = eye(6,1)+(sqrt(finfo(float).eps)/1000)*randn(6,1)
x8 = -x7
e1 = eye(6,1)
vector_count = 1 #contador para colocarle numero a las Xi de la tabla

#Inicializar una lista de vectores a procesar para poder sacar la informacion necesaria
list_Vectores = list()
list_Vectores.append(x1)
list_Vectores.append(x2)
list_Vectores.append(x3)
list_Vectores.append(x4)
list_Vectores.append(x5)
list_Vectores.append(x6)
list_Vectores.append(x7)
list_Vectores.append(x8)

t = Texttable() # create the table to put the data inside
t.set_deco(Texttable.HEADER)
t.set_cols_dtype([            't',  # text
                              't',  # text
                              'e',  # float (exponent)
                              'e',  # float (exponent)
                              'e',  # float (exponent)
                              'e']) # float (exponent) 
t.set_cols_align(["c","c","c","c","c","c"])
t.add_rows([['Xi',
             'signo(xi)',
             '||PHi xi - alphai e1||2',
             '||I - PHi.T PHi||2',
             '||NHi xi + alphai e1||2', 
             '||I - NHi.T NH||2']])


for i in list_Vectores:
    argumentos_tabla = list()
    argumentos_tabla.append('X{}'.format(vector_count))
    vector_count += 1
    if np.sign(i[0][0]) == 1:
        argumentos_tabla.append('+')
    else:
        argumentos_tabla.append('-')
        
    #Comienzo de las Operacion con la matriz HH positiva
    PHH , alphaP = PH(i,e1)
    argumentos_tabla.append(np.linalg.norm(np.dot(PHH,i) - np.dot(alphaP,e1)))
    argumentos_tabla.append(np.linalg.norm(I - np.dot(PHH.transpose(),PHH)))
    
    #comienzo de las operaciones con la matriz HH negativa
    NHH , alphaN = NH(i,e1)
    argumentos_tabla.append(np.linalg.norm(np.dot(NHH,i) - np.dot(alphaN,e1)))
    argumentos_tabla.append(np.linalg.norm(I - np.dot(NHH.transpose(),NHH)))
    
    t.add_row([argumentos_tabla[0],
                argumentos_tabla[1],
                argumentos_tabla[2],
                argumentos_tabla[3],
                argumentos_tabla[4],
                argumentos_tabla[5]])

print(t.draw())

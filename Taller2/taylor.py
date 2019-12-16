# -*- coding: utf-8 -*-
import numpy as np
import sympy as sym

def politaylor(funcionx,x0,n):
    k = 0
    polinomio = 0
    while (k <= n):
        derivada   = funcionx.diff(x,k)
        derivadax0 = derivada.subs(x,x0)
        divisor   = np.math.factorial(k)
        terminok  = (derivadax0/divisor)*(x-x0)**k
        polinomio = polinomio + terminok
        k = k + 1
    return(polinomio)
    
x = sym.Symbol('x')
funcionx = (-1/6*x**2) / (2+3)*(2+2)

x0 = 0          
n  = 10         # Grado polinomio Taylor
a  = -5 ; b = 5  # x entre [a,b]
muestras = 51

# PROCEDIMIENTO
# tabla polinomios
px_tabla = []
for grado in range(0,n,1):
    polinomio = politaylor(funcionx,x0,grado)
    px_tabla.append(polinomio)

# SALIDA
print('grado :  polinomio')
for grado in range(0,n,1):
    px = px_tabla[grado]
    print(str(grado)+ ' : '+str(px))
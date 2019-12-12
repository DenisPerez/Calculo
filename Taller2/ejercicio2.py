# -*- coding: utf-8 -*-
import numpy as np

n = 255
x = np.array([0.2]*n)
norma1 = 0
print(x)

for k in range(0, n):
    norma1 = norma1 + x[k]
    print(np.abs(x[k]))
print(norma1)
if norma1 == (0.2*n):
    print(0.2*n)
    print("Calcule la norma 1 de x")
else:
    print(0.2*n)
    print("Algo esta extrano")

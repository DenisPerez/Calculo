# -*- coding: utf-8 -*-
import numpy as np


acum = np.log(6/5)
print(acum)
n = 0


for i in range(5,25,5):
    acum = (1/i)-(5*acum)
    print(acum)
    
for i in range(30,70,10):
    acum = (1/i)-(5*acum)
    print(acum)
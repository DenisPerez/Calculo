# -*- coding: utf-8 -*-
import numpy as np


acum = np.log(6/5)
n = 0

for i in range(5,25,5):
    acum = (1/i)-(5*acum)
    #print(i,":", acum)
    
for i in range(30,70,10):
    acum = (1/i)-(5*acum)
    #print(i, acum)
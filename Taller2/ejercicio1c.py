# -*- coding: utf-8 -*-
import numpy as np


acum = np.log(6/5)
print(acum)
n = 0

for i in range(1,20):
    acum = (1/i)-(5*acum)
    print(acum)

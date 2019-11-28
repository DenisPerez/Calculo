# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import scipy as s

acum = np.log(6/5)
print(acum)
n = 0

for i in range(1,20):
    acum = (1/i)-(5*acum)
    print(acum)

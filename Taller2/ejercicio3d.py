# -*- coding: utf-8 -*-
import scipy.linalg as sla
import numpy as np

A = np.array([[0.4,-0.6,0.2],[-0.3,0.7,-0.4],[-0.1,-0.4,0.5]])
x = np.array([[1],[1],[1]])
S,U=sla.eig(A)
print(S.max())
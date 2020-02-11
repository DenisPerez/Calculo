# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as sla
from texttable import Texttable
from pprint import pprint
import scipy as sp

e1 =[10.0, 10**-2, 10**-4, 10**-8, 10**-10]

e_variable = np.random.rand()

A = np.array([[1.,1.,1.],[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
b = np.array([[3],[0],[0],[0]])

#L = np.linalg.cholesky(A)
Q,R = sp.linalg.qr(A)
A,B = sp.linalg.qr(A,mode = 'economic')
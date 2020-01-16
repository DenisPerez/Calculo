# -*- coding: utf-8 -*-
import numpy as np # numpy import
from pprint import pprint


T = np.array([[-10.83,0,0],
              [7,-13.9352,0],
              [4,7.1286,2.2947],
              [3,11.3464,2.0894]
              ])


(num_rows, num_cols) = np.shape(T)


W = np.empty([4,2])
Y = np.empty([4,2])


u1 = np.array([T[0:, 0]])

p1 = -2/(np.dot(u1.transpose(),np.matrix.conjugate(np.array(u1))))

tt = np.dot(p1,u1.transpose())
W[:,0:1] = tt.reshape(4,1)
Y[:,0:1] = u1.reshape(4,1)

for j in range(1,num_cols):
    u1 = np.array([T[j:, j]])
    p = -2/(np.dot(u1.transpose(),np.matrix.conjugate(np.array(u1))))
    
    z = np.dot(np.dot(p,np.identity(4) + np.dot(W,np.matrix.conjugate(Y))),u1)

    W[:,0:1] = z.reshape(4,1)
    Y[:,0:1] = u1.reshape(4,1)
    
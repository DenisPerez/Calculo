import numpy as np

f = lambda x : (x-np.sin(x))/(x**3)
fvalues = []
def evaluatef(n):
    x = 1
    for i in range(1,n+1):
        if i == 1:
            fvalues.append(f(1))
        else:
            x = (1/10)*x
            fvalues.append(f(x))
evaluatef(60) 
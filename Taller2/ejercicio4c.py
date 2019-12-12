# -*- coding: utf-8 -*-

def f(i, x, t): return (-t*x**2)/((2*i + 2)*(2*i + 3))


fvalues = []
tvalues = []

def aproxf(n=10, t=1/6, _f=1/6):
    x = 1/10
    for i in range(2, 11):
        if i == 2:
            t = f(i, 1, t)
            _f = _f + t
            tvalues.append(t)
            fvalues.append(_f)
        else:
            x = (1/10)*x
            t = f(i, x, t)
            _f = _f + t
            tvalues.append(t)
            fvalues.append(_f)
aproxf()

# This is a very useless code, dont use it.

import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return 1 / (1 + 25*x**2)

def piecewise(a, b, order):
    xi = np.linspace(a, b, order+1)
    fx = [f(x) for x in xi]  # The reason that it's useless is that we can directly plot xi and fx to get the same result
    d = [(fx[i+1] - fx[i]) / (xi[i+1] - xi[i]) for i in range(order)]
    
    funclist = []
    
    for i in range(order):
        def q(x, i=i): return fx[i] + d[i]*(x-xi[i])
        funclist.append(q)

    x = np.linspace(a, b, 1000)
    y = np.piecewise(x, [np.logical_and(x >= xi[i], x <= xi[i+1]) for i in range(order)], funclist)
    
    plt.plot(x, y)
    plt.plot(xi, fx, 'ro')
    plt.show()

piecewise(-1, 1, 10)
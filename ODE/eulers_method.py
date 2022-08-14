import numpy as np
from matplotlib import pyplot as plt

def f(y, x=0):  # x is in case of some function with x
    return 1-4*y

def euler(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n+1)
    h = (stop - t0)/n
    
    for i in range(n):
        y.append(y[i] + h*f(y[i], x[i]))

    plt.plot(x, y)
    plt.show()

euler(0, 3, 10, 1000)
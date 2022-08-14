import numpy as np
from matplotlib import pyplot as plt

def f(y, x=0):
    return -y*np.log(y)

def rk2(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n+1)
    h = (stop - t0)/n
    
    for i in range(n):
        k1 = f(y[i], x[i])
        k2 = f(y[i] + h*k1, x[i] + h)
        y.append(y[i] + h/2*(k1 + k2))

    plt.plot(x, y)
    plt.show()

rk2(0, 0.5, 10, 40)
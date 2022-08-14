import numpy as np
from matplotlib import pyplot as plt

def f(y, x=0):
    return -y*np.log(y)

def abm(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n+1)
    h = (stop - t0)/n
    
    for i in range(3):
        y.append(y[i] + h*f(y[i], x[i]))  # Euler

    for i in range(3, n):
        y.append(y[i-3] + 4/3*h*(2*f(y[i], x[i]) - f(y[i-1], x[i-1]) + 2*f(y[i-2], x[i-2])))  # Predictor
        y[i+1] = y[i-1] + h/3*(f(y[i-1], x[i-1]) + 4*f(y[i], x[i]) + f(y[i+1], x[i+1]))  # Corrector

    plt.plot(x, y)
    plt.show()

abm(0, 3, 10, 1000)
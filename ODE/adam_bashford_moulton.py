import numpy as np
from matplotlib import pyplot as plt

def f(y, x=0):
    return 1-4*y

def abm(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n+1)
    h = (stop - t0)/n
    
    for i in range(3):
        y.append(y[i] + h*f(y[i], x[i]))  # Euler

    for i in range(3, n):
        y.append(y[i] + h/24*(55*f(y[i], x[i]) - 59*f(y[i-1], x[i-1]) + 37*f(y[i-2], x[i-2]) - 9*f(y[i-3], x[i-3])))  # Predictor
        y[i+1] = y[i] + h/24*(9*f(y[i+1], x[i+1]) + 19*f(y[i], x[i]) - 5*f(y[i-1], x[i-1]) + f(y[i-2], x[i-2]))  # Corrector
    
    plt.plot(x, y)
    plt.show()

abm(0, 1, 1, 1000)
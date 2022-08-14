import numpy as np
from matplotlib import pyplot as plt

def f(y, thalf):
    lamb = np.log(2)/thalf
    return -y*lamb

def real(t0, y0, stop, n, thalf):
    lamb = np.log(2)/thalf
    x = np.linspace(t0, stop, n)
    y = y0*np.exp(-lamb*x)

    plt.plot(x, y, label='Real')

def euler(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n)
    h = (stop - t0)/(n-1)
    
    for i in range(n-1):
        y.append(y[-1] + h*f(y[-1], 5))

    plt.plot(x, y, label='euler')

def rk2(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n)
    h = (stop - t0)/(n-1)
    
    for i in range(n-1):
        k1 = f(y[-1], 5)
        k2 = f(y[-1] + h*k1, 5)
        y.append(y[-1] + h/2*(k1 + k2))

    plt.plot(x, y, label='rk2')

def rk4(t0, y0, stop, n):
    y = [y0]
    x = np.linspace(t0, stop, n)
    h = (stop - t0)/(n-1)
    
    for i in range(n-1):
        k1 = f(y[-1], 5)
        k2 = f(y[-1] + h/2*k1, 5)
        k3 = f(y[-1] + h/2*k2, 5)
        k4 = f(y[-1] + h*k3, 5)
        y.append(y[-1] + h/6*(k1 + 2*k2 + 2*k3 + k4))

    plt.plot(x, y, label='rk4')
    plt.legend()
    plt.show()

real(0, 10, 10, 5, 5)
euler(0, 10, 10, 5)
rk2(0, 10, 10, 5)
rk4(0, 10, 10, 5)
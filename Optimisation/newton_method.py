from scipy.misc import derivative
from math import sin, cos

def f(x):
    return x**2/10 - 2*sin(x)

def fp(x):
    return x/5 - 2*cos(x)

def fpp(x):
    return 1/5 + 2*sin(x)

def newton(x0, error):
    while True:
        x1 = x0 - fp(x0)/fpp(x0)
        delx = abs(x1 - x0)

        if delx < error:
            return x1, delx
        
        x0 = x1

print(newton(1, 1e-5))
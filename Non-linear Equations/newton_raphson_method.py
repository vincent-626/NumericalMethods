from scipy.misc import derivative
import numpy as np

def f(x):
    return x + np.tan(x)

def fp(x):
    return derivative(f, x, dx=1e-9)

def newton_raphson(x0, error):
    while True:
        x1 = x0 - f(x0)/fp(x0)
        delx = abs(x1 - x0)

        if delx < error:
            return x1, delx
        
        x0 = x1

print(newton_raphson(3, 1e-6))
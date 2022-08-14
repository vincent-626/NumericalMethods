import numpy as np

def f(x):
    return x*np.log(x)

def basic_simpson(a, b):
    h = (b-a)/2

    return h/3*(f(a) + 4*f((a+b)/2) +f(b))

print(basic_simpson(1, 2))
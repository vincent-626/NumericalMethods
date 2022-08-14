import numpy as np

def f(x):
    return x*np.log(x)

def basic_trapezoid(a, b):
    return (b-a)/2*(f(a) + f(b))

print(basic_trapezoid(1, 2))
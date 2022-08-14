import numpy as np

def f(x):
    return x*np.log(x)

def basic_midpoint(a, b):
    return (b-a)*f((a+b)/2)

print(basic_midpoint(1, 2))
import numpy as np

def f(x):
    return x*np.log(x)

def comp_midpoint(a, b, n):
    h = (b-a)/n
    total = 0

    for i in range(1, n+1):
        total += f(a + (i - 0.5)*h)

    return h*total

print(comp_midpoint(1, 2, 1000))
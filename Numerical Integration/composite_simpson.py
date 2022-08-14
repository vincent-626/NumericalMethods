import numpy as np

def f(x):
    return x*np.log(x)

def comp_simpson(a, b, n):
    x = np.linspace(a, b, n+1)
    total = 0

    for i in range(1, n//2+1):
        hi = (x[2*i] - x[2*i - 2])/2
        total += hi/3*(f(x[2*i-2]) + 4*f(x[2*i-1]) + f(x[2*i]))

    return total

print(comp_simpson(1, 2, 1000))
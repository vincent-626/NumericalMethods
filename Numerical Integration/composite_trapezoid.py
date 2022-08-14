import numpy as np

def f(x):
    return x*np.log(x)

def trapezoid(a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    total = 0

    for i in range(1, n-1):
        total += f(x[i])
    
    ans = h/2*(f(x[0]) + 2*total + f(x[n]))

    return ans

print(trapezoid(1, 2, 10000))
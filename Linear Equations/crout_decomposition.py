# Crout decomposition

import numpy as np
from scipy import linalg

def crout(a):
    n = len(a)
    l = np.identity(n)
    u = np.identity(n)

    for i in range(n):  # each row for upper and each column for lower
        # Lower triangle
        for k in range(i, n):
            total = 0
            for j in range(i):
                total += l[k][j]*u[j][i]
            l[k][i] = a[k][i] - total        
        
        # Upper triangle
        for k in range(n-1, i, -1):
            total = 0
            for j in range(i):
                total += l[i][j]*u[j][k]
            u[i][k] = (a[i][k] - total)/l[i][i]

    return l, u

A = np.array([
    [-4, 1, 1, 0],
    [1, -4, 0, 1],
    [1, 0, -4, 1],
    [0, 1, 1, -4]
])

l, u = crout(A)
print('The lower triangle:\n', l, '\n\nThe upper triangle:\n', u)

b = [-1.6449, -1.6449, -1.6449, -1.6449]

y = linalg.solve(l, b)
x = linalg.solve(u, y)
print(y)
print(x)
# Doolittle decomposition

import numpy as np

def doolittle(a):
    n = len(a)
    l = np.identity(n)
    u = np.identity(n)

    for i in range(n):  # each row for upper and each column for lower
        # Upper triangle
        for k in range(i, n):  # each element in the row
            total = 0
            for j in range(i):
                total += l[i][j]*u[j][k]  # sum of the terms along the kth column
            u[i][k] = a[i][k] - total
        
        # Lower triangle
        for k in range(i+1, n):  # each element in the column
            total = 0
            for j in range(i):
                total += l[k][j]*u[j][i]  # sum of the terms along the kth row
            l[k][i] = (a[k][i] - total)/u[i][i]
    
    return l, u

A = np.array([
    [10, -7, 0],
    [-3, 2, 6],
    [5, -1, 5]
])

l, u = doolittle(A)
print('The lower triangle:\n', l, '\n\nThe upper triangle:\n', u)
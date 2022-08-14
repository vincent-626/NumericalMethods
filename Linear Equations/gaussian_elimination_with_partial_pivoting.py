import numpy as np  # Not necessary to use numpy, I used it simply for better presentation of my matrix

def gaussian(a, b):
    n = len(a)
    x = np.empty(n)

    # Gaussian Elimination with Partial Pivoting
    for i in range(1, n):  # for each row (skip row 0)
        # Partial Pivoting
        am = abs(a[i][i])
        p = i
    
        for j in range(i+1, n):
            if abs(a[j][i]) > am:
                am = abs(a[j][i])
                p = j
    
        if p > i:
            temp1 = list(a[i])
            a[i] = a[p]
            a[p] = temp1

            temp2 = float(b[i])
            b[i] = b[p]
            b[p] = temp2
    
        # Gaussian Elimination
        for j in range(i):  # for each operation in each row (ith row needs i operations)
            m = a[i][j]/a[j][j]
            b[i] -= m*b[j]
            for k in range(j+1, n):  # for each element in a row (k represents column) (zero terms are skipped to save time)
                a[i][k] -= m*a[j][k]

    # Backward Solution
    x[n-1] = b[n-1]/a[n-1][n-1]  # last x

    for i in range(n-2, -1, -1):
        total = 0
        for j in range(i+1, n):
            total += a[i][j]*x[j]
        x[i] = (b[i] - total)/a[i][i]

    return x

a = np.array([
            [21., 67., 88., 73.],
            [76., 63., 7., 20.],
            [0., 85., 56., 54.],
            [19.3, 43., 30.2, 29.4]
])

b = np.array([141., 109., 218., 93.7])

print(gaussian(a, b))
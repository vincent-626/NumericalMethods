import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_excel('lsdata1.xlsx')
t = df['Temperature']
c = df['Conductance']
n = len(t)

sum_x = sum(t)
sum_y = sum(c)

sum_x2 = 0
sum_xy = 0

for i in range(n):
    sum_x2 += t[i]**2
    sum_xy += t[i]*c[i]

m = (n*sum_xy -  sum_x*sum_y) / (n*sum_x2 - sum_x**2)
b = (sum_x2*sum_y - sum_x*sum_xy) / (n*sum_x2 - sum_x**2)

x = np.linspace(t[0], t[n-1], 1000)
y = m*x + b

plt.plot(x, y, label='Regression Line')
plt.plot(t, c, 'ro', label='Data')
plt.title('Temperature against Conductance of Iron')
plt.grid(True)
plt.legend()
plt.show()
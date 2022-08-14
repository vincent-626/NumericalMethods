import numpy as np
import pandas as pd
from scipy.stats import linregress
from matplotlib import pyplot as plt

df = pd.read_excel('lsdata1.xlsx')
t = df['Temperature']
c = df['Conductance']

line = linregress(t, c)
m = line.slope
b = line.intercept

x = np.linspace(t[0], t[len(t)-1], 1000)
y = m*x +b

plt.plot(x, y, label='Regression Line')
plt.plot(t, c, 'ro', label='Data')
plt.title('Temperature against Conductance of Iron')
plt.grid(True)
plt.legend()
plt.show()
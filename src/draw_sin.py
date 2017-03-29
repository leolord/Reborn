u"""
使用matplog画图
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

plt.style.use('bmh')
print(plt.style.available, sep='\n')

x = np.linspace(0, 10, 8)
y = np.sin(x)

func = interpolate.interp1d(x, y, kind='cubic')

x_interp = np.linspace(0, 10, 1000)
y_interp = func(x_interp)


plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp)
plt.show()

import numpy as np
from  matplotlib import  pyplot as plt

fig = plt.figure()

x = np.linspace(-5,5, 1000)

y= x-2
z= 2*x-3

w=3*x-4

ax = plt.gca()
ax.plot(x, y)
ax.plot(x, z)
ax.plot(x, w)

ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


plt.show()

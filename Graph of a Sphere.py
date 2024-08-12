from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(1)
ax = fig.add_subplot(projection='3d')

u = np.linspace(0, 2*np.pi, 40)
v = np.linspace(0, np.pi, 40)

xv, yv = np.meshgrid(u, v, indexing='ij', sparse=True)

x = np.cos(xv)*np.sin(yv)
y = np.sin(xv)*np.sin(yv)
z = np.cos(yv)

ax.plot_surface(x, y, z, cmap=cm.coolwarm)

ax.set_aspect('equal')
plt.show()
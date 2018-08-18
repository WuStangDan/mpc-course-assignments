from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-0, 10, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
def cost_function(x,y):
    x_obs = 5
    y_obs = 0
    x_goal = 10
    y_goal = 0
    z = np.copy(x)
    for i in range(len(x)):
        for j in range(len(y)):
            distance = (x[i,j] - x_obs)**2 + (y[i,j] - y_obs)**2
            distance = np.sqrt(distance)
            z[i,j] = 1/max(distance,0.3)*10
            z[i,j] += (x[i,j] - x_goal)**2
            z[i,j] += (y[i,j] - y_goal)**2
    return z



Z = cost_function(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

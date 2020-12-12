import numpy as np
from scipy import stats
from mayavi import mlab

mu, sigma = 0, 0.1
x = 10*np.random.normal(mu, sigma, 250000)
y = 10*np.random.normal(mu, sigma, 250000)
z = 10*np.random.normal(mu, sigma, 250000)

print(x.shape)
print(y.shape)
print(z.shape)
xyz = np.vstack([x, y, z])
print(xyz.shape)
kde = stats.gaussian_kde(xyz)
density = kde(xyz)

# Plot scatter with mayavi
figure = mlab.figure('DensityPlot')
pts = mlab.points3d(x, y, z, density, scale_mode='none', scale_factor=0.07)
mlab.axes()
mlab.show()

import numpy as np
import matplotlib.pyplot as plt
import cv2
#3*3 Gassian filter
x, y = np.mgrid[-1:2, -1:2]
gaussian_kernel = np.exp(-(x**2+y**2))

#Normalization
gaussian_kernel = gaussian_kernel / gaussian_kernel.sum()
print(gaussian_kernel)

print(cv2.getGaussianKernel(3, 0))

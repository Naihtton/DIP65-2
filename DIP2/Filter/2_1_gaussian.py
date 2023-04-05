import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Get image dimensions
X, Y = img.shape

# Compute Fourier transform
img_fft = np.fft.fft2(img)

# Display original image
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

# Compute distances in frequency domain
u = np.arange(X)
v = np.arange(Y)
u[np.where(u > X/2)] -= X
v[np.where(v > Y/2)] -= Y
U, V = np.meshgrid(u, v)
D = np.sqrt(U**2 + V**2)

# Gaussian lowpass filter
sigma_values = [10, 20, 30, 40, 50]
for i, sigma in enumerate(sigma_values):
    H_glf = np.exp(-(D**2)/(2*sigma**2))
    G_glf = H_glf * img_fft
    glf = np.fft.ifft2(G_glf)
    plt.subplot(2, 3, i+2)
    plt.imshow(np.abs(glf), cmap='gray')
    plt.title('Gaussian lowpass filter ({})'.format(sigma))

plt.show()

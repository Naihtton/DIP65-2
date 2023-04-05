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
plt.title('origin')

# Compute distances in frequency domain
u = np.arange(X)
v = np.arange(Y)
u[np.where(u > X/2)] -= X
v[np.where(v > Y/2)] -= Y
U, V = np.meshgrid(u, v)
D = np.sqrt(U**2 + V**2)

# Ideal low pass filter
H10 = np.double(D <= 10)
G10 = H10 * img_fft
ideal10 = np.fft.ifft2(G10)
plt.subplot(2, 3, 2)
plt.imshow(np.abs(ideal10), cmap='gray')
plt.title('ideal low pass (10)')

H20 = np.double(D <= 20)
G20 = H20 * img_fft
ideal20 = np.fft.ifft2(G20)
plt.subplot(2, 3, 3)
plt.imshow(np.abs(ideal20), cmap='gray')
plt.title('ideal low pass (20)')

H30 = np.double(D <= 30)
G30 = H30 * img_fft
ideal30 = np.fft.ifft2(G30)
plt.subplot(2, 3, 4)
plt.imshow(np.abs(ideal30), cmap='gray')
plt.title('ideal low pass (30)')

H40 = np.double(D <= 40)
G40 = H40 * img_fft
ideal40 = np.fft.ifft2(G40)
plt.subplot(2, 3, 5)
plt.imshow(np.abs(ideal40), cmap='gray')
plt.title('ideal low pass (40)')

H50 = np.double(D <= 50)
G50 = H50 * img_fft
ideal50 = np.fft.ifft2(G50)
plt.subplot(2, 3, 6)
plt.imshow(np.abs(ideal50), cmap='gray')
plt.title('ideal low pass (50)')


plt.show()

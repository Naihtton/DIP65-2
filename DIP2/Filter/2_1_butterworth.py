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

# Butterworth lowpass filter
cutoff = 10
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 3, 2)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (10, 2)')

cutoff = 20
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 3, 3)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (20, 2)')

cutoff = 30
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 3, 4)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (30, 2)')

cutoff = 40
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 3, 5)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (40, 2)')

cutoff = 50
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 3, 6)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (50, 2)')

plt.show()

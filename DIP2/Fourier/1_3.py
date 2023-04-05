import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Define the rotation matrix
rows, cols = ima.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)

# Rotate the image
rotated = cv2.warpAffine(ima,M,(cols,rows))

# Compute the Fourier transform
imagefft = np.fft.fft2(np.float32(rotated))

# Shift the Fourier transform
shiftedfft = np.fft.fftshift(imagefft)

# Compute the magnitude and phase spectra
amp = np.log(np.abs(shiftedfft))
phase = np.angle(shiftedfft)

# Display the results
plt.subplot(121), plt.imshow(amp, cmap='gray')
plt.title('Amplitude spectrum rotated'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(phase, cmap='gray')
plt.title('Phase spectrum rotated'), plt.xticks([]), plt.yticks([])
plt.show()

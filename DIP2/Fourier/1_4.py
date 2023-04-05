import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Downsample the image to 100x100 using OpenCV resize function
ima = cv2.resize(ima, (100, 100))

# Compute the Fourier transform
imagefft = np.fft.fft2(np.float32(ima))

# Shift the Fourier transform
shiftedfft = np.fft.fftshift(imagefft)

# Compute the magnitude and phase spectra
amp = np.log(np.abs(shiftedfft))
phase = np.angle(shiftedfft)

# Display the results
plt.subplot(121), plt.imshow(amp, cmap='gray')
plt.title('Amplitude spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(phase, cmap='gray')
plt.title('Phase spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

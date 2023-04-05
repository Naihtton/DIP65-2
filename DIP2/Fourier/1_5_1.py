import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Pad the image to 256x256 (closet 2^n)
padimage = cv2.copyMakeBorder(ima, 28, 28, 28, 28, cv2.BORDER_CONSTANT, value=0)

# Compute the Fourier transform
imagefft = np.fft.fft2(np.float32(padimage))

# Set the phase data to zero
shiftedfft_zero_phase = np.abs(imagefft) * np.exp(0j * np.angle(imagefft))

# Inverse shift the Fourier transform
shift_idft_zero_phase = np.fft.ifftshift(shiftedfft_zero_phase)

# Inverse Fourier transform
image_zero_phase = np.fft.ifft2(shift_idft_zero_phase)

# Take the real part of the image
image_zero_phase = np.real(image_zero_phase)

# Display the result
plt.imshow(image_zero_phase, cmap='gray')
plt.title('Image with no phase')
plt.show()

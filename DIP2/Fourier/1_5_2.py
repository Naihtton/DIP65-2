import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Pad the image to 256x256 (closet 2^n)
padimage = cv2.copyMakeBorder(ima, 28, 28, 28, 28, cv2.BORDER_CONSTANT, value=0)

# Compute the Fourier transform
imagefft = np.fft.fft2(np.float32(padimage))

# Set the amplitude data to one
shiftedfft_one_amp = np.exp(1j * np.angle(imagefft))

# Inverse shift the Fourier transform
shift_idft_one_amp = np.fft.ifftshift(shiftedfft_one_amp)

# Inverse Fourier transform
image_one_amp = np.fft.ifft2(shift_idft_one_amp)

# Take the real part of the image
image_one_amp = np.real(image_one_amp)

# Display the result
plt.imshow(image_one_amp, cmap='gray')
plt.title('Image with no amplitude')
plt.show()

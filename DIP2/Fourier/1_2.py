import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima = cv2.imread('Cross.pgm', cv2.IMREAD_GRAYSCALE)

# Pad the image to 256x256 (closet 2^n)
padimage = cv2.copyMakeBorder(ima, 28, 28, 28, 28, cv2.BORDER_CONSTANT, value=0)

# Compute the Fourier transform
imagefft = np.fft.fft2(np.float32(padimage))

# Shift the Fourier transform
shiftedfft = np.fft.fftshift(imagefft)

# Compute the magnitude and phase spectra
amp = np.log(np.abs(shiftedfft))
phase = np.angle(shiftedfft)

# Multiply the phase spectrum by a complex number to shift the image
shift_phase = np.zeros_like(shiftedfft)
shift_phase[30, 20] = 1
shift_phase = np.exp(1j * np.angle(np.fft.ifftshift(shift_phase)))
shiftedfft *= shift_phase

# Inverse shift the Fourier transform
shift_idft = np.fft.ifftshift(shiftedfft)

# Inverse Fourier transform
shift_idft = np.fft.ifft2(shift_idft)

# Take the real part of the image
shift_idft = np.real(shift_idft)

# Display the shifted image
plt.imshow(shift_idft, cmap='gray')
plt.title('Shifted image')
plt.show()

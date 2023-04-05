import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
ima_chess = cv2.imread('Chess.pgm', cv2.IMREAD_GRAYSCALE)

# Define a small kernel
kernel = np.ones((3,3)) / 9

# Perform convolution on the image
ima_conv = cv2.filter2D(ima_chess, -1, kernel)

# Compute the Fourier transform of the kernel
kernel_fft = np.fft.fft2(kernel, s=ima_chess.shape)

# Shift the Fourier transform
shifted_kernel_fft = np.fft.fftshift(kernel_fft)

# Compute the Fourier transform of the image
ima_fft = np.fft.fft2(np.float32(ima_chess))

# Shift the Fourier transform
shifted_ima_fft = np.fft.fftshift(ima_fft)

# Filter in frequency domain
ima_blur_fft = shifted_ima_fft * shifted_kernel_fft

# Inverse shift the Fourier transform
ima_blur_ifft = np.fft.ifftshift(ima_blur_fft)

# Inverse Fourier transform
ima_blur_ifft = np.fft.ifft2(ima_blur_ifft)

# Take the absolute value of the image
ima_blur_ifft = np.abs(ima_blur_ifft)

# Display the results
plt.subplot(131), plt.imshow(ima_chess, cmap='gray')
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(ima_conv, cmap='gray')
plt.title('Convolution'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(ima_blur_ifft, cmap='gray')
plt.title('Frequency domain'), plt.xticks([]), plt.yticks([])
plt.show()

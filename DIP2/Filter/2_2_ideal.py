import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('Lenna_noise.pgm', cv2.IMREAD_GRAYSCALE)

# Get image dimensions
X, Y = img.shape

# Compute Fourier transform
img_fft = np.fft.fft2(img)

# Display original image
plt.subplot(2, 2, 1)
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
plt.subplot(2, 2, 2)
plt.imshow(np.abs(ideal10), cmap='gray')
plt.title('ideal low pass (10)')

H30 = np.double(D <= 30)
G30 = H30 * img_fft
ideal30 = np.fft.ifft2(G30)
plt.subplot(2, 2, 3)
plt.imshow(np.abs(ideal30), cmap='gray')
plt.title('ideal low pass (30)')

H50 = np.double(D <= 50)
G50 = H50 * img_fft
ideal50 = np.fft.ifft2(G50)
plt.subplot(2, 2, 4)
plt.imshow(np.abs(ideal50), cmap='gray')
plt.title('ideal low pass (50)')



plt.show()

#RMS calculate
def compare_cutoff_levels(image_path, cutoff_freqs):
    # Load image with noise
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Compute Fourier transform
    img_fft = np.fft.fft2(img)

    # Compute distances in frequency domain
    X, Y = img.shape
    u = np.arange(X)
    v = np.arange(Y)
    u[np.where(u > X/2)] -= X
    v[np.where(v > Y/2)] -= Y
    U, V = np.meshgrid(u, v)
    D = np.sqrt(U**2 + V**2)
    
    # Calculate RMS errors for each cutoff frequency
    rms_errors = []
    for cutoff_freq in cutoff_freqs:
        H = np.double(D <= cutoff_freq)
        G = H * img_fft
        filtered_img = np.fft.ifft2(G).real
        
        # Compute RMS error
        error = np.sqrt(np.mean((img - filtered_img)**2))
        rms_errors.append(error)
    
    return rms_errors

cutoff_freqs = [10, 30, 50]
rms_errors = compare_cutoff_levels('Lenna.pgm', cutoff_freqs)
print(rms_errors)


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
plt.subplot(2, 2, 2)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (10, 2)')


cutoff = 30
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 2, 3)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (30, 2)')


cutoff = 50
n = 2
H_blf = 1 / (1 + (D / cutoff)**(2*n))
G_blf = H_blf * img_fft
blf = np.fft.ifft2(G_blf)
plt.subplot(2, 2, 4)
plt.imshow(np.abs(blf), cmap='gray')
plt.title('Butterworth lowpass filter (50, 2)')

plt.show()

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
        n = 2
        H = 1 / (1 + (D / cutoff_freq)**(2*n))
        G = H * img_fft
        filtered_img = np.fft.ifft2(G).real
        
        # Compute RMS error
        error = np.sqrt(np.mean((img - filtered_img)**2))
        rms_errors.append(error)
    
    return rms_errors

cutoff_freqs = [10, 30, 50]
rms_errors = compare_cutoff_levels('Lenna.pgm', cutoff_freqs)
print(rms_errors)

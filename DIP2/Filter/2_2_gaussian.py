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

# Gaussian lowpass filter
sigma_values = [10, 30, 50]
for i, sigma in enumerate(sigma_values):
    H_glf = np.exp(-(D**2)/(2*sigma**2))
    G_glf = H_glf * img_fft
    glf = np.fft.ifft2(G_glf)
    plt.subplot(2, 2, i+2)
    plt.imshow(np.abs(glf), cmap='gray')
    plt.title('Gaussian lowpass filter ({})'.format(sigma))

plt.show()

#RMS calculate
def compare_cutoff_levels(image_path, sigma_values):
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
    for sigma in sigma_values:
        H = np.exp(-(D**2)/(2*sigma**2))
        G = H * img_fft
        filtered_img = np.fft.ifft2(G).real
        
        # Compute RMS error
        error = np.sqrt(np.mean((img - filtered_img)**2))
        rms_errors.append(error)
    
    return rms_errors

sigma_values = [10, 30, 50]
rms_errors = compare_cutoff_levels('Lenna.pgm', sigma_values)
print(rms_errors)

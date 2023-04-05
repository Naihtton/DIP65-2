import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ToGrayscale(img):
    return np.dot(np.array(img, dtype='float32'), [0.25, 0.25, 0.25])

# Load image and convert to grayscale
img = Image.open('WormHole_2H.tif')
gray = ToGrayscale(img)

# Apply binary threshold to segment wormholes
threshold = 35
binary = np.zeros_like(gray)
binary[gray < threshold] = 1

# Display original, grayscale, and segmented images
fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].imshow(gray, cmap='gray')
axs[0].set_title('Grayscale')
axs[1].imshow(binary, cmap='gray')
axs[1].set_title('Segmented')
plt.show()

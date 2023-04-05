import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image and convert to grayscale
src = 'WormHole_2H.tif'
org_img = Image.open(src)
img = Image.open(src).convert('L')
img = np.array(img)

# Apply binary threshold to segment wormholes
thresh = 50
binary = np.zeros_like(img)
binary[img < thresh] = 1

# Display original and segmented images
fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].imshow(org_img, cmap='gray')
axs[0].set_title('Original')
axs[1].imshow(img, cmap='gray')
axs[1].set_title('Grayscaled')
plt.show()

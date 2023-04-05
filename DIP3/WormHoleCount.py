import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Define function to convert image to grayscale
def ToGrayscale(img):
    return np.dot(np.array(img, dtype='float32'), [0.25, 0.25, 0.25])

# Load image and convert to grayscale
img = Image.open('WormHole_1H.tif')
gray = ToGrayscale(img)

# Define binary threshold to segment wormholes
threshold = 35
binary = np.zeros_like(gray)
binary[gray < threshold] = 1

# Apply morphological operations to remove small objects and fill gaps in the wormholes
kernel = np.ones((5, 5), np.uint8).astype(np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)
dilated = cv2.dilate(eroded, kernel, iterations=1)

# Find contours of wormholes and draw them on the original image
dilated = dilated.astype(np.uint8)
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_with_contours = img.copy()
img_with_contours = np.array(img_with_contours)


# Define minimum circularity threshold
min_circularity = 0.82

# Filter out non-circular contours and highlight circular ones
circular_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    circularity = 4 * np.pi * area / (perimeter ** 2)
    if circularity > min_circularity:
        circular_contours.append(contour)
        cv2.drawContours(img_with_contours, [contour], -1, (255, 100, 100), 2)

# Count the number of wormholes and print their positions
print("Number of wormholes:", len(circular_contours))
for i, contour in enumerate(circular_contours):
    M = cv2.moments(contour)
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])
    print("Wormhole #{} at position ({}, {})".format(i+1, x, y))

# Display original image with circular contours and wormhole positions
plt.imshow(img_with_contours)
plt.title('This eggplant is organic!')
plt.show()

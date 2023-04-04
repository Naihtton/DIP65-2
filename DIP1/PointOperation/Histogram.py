import matplotlib.pyplot as plt
import numpy as np

# Open the PGM image in binary mode
with open('Cameraman.pgm', 'rb') as f:
    # Read the header
    f.readline() # skip the P5 magic number
    width, height = map(int, f.readline().split())
    max_val = int(f.readline())

    # Read the pixel values into a 2D array
    pixels = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(int.from_bytes(f.read(1), byteorder='big'))
        pixels.append(row)

# Flatten the pixel values into a 1D array
pixels_flat = np.array(pixels).flatten()

# Plot the histogram
plt.hist(pixels_flat, bins=range(max_val+2))
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()

#!/bin/env/python

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["figure.figsize"] = (5.0, 5.0)

# Load in the data
img = cv2.imread("./A5_1.png")
original = img.copy()
# Grab the green color layer from the image
image1 = original[:, :, 1]
# Conver the image to grayscale
image2 = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

plt.imshow(image2)
plt.show()


# Set a threshold for the image
th, img_thresh = cv2.threshold(image1, 150, 255, cv2.THRESH_BINARY)

im1 = img_thresh
im2 = image1
dst = cv2.addWeighted(im1, 0.5, im2, 0.7, 0)
img_arr = np.vstack((im1, im2))

plt.imshow(img_arr)
plt.show()

contours, hierarchy = cv2.findContours(im1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

print(contours)

print(len(contours))


new = cv2.drawContours(original, contours, -1, (0, 255, 0), 3)

plt.imshow(new)
plt.show()

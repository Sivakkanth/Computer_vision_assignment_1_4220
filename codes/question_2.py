########################################################################
#   Take Home Assignment 1
#   Question 2
#   Reg No: EG/2020/4220
#   Date: 2025-06-16
########################################################################

# Import required libraries
import cv2
import numpy as np

# Read the image
img = cv2.imread("image/image1.jpg")

# check if the image is loaded successfully
if img is None:
    raise ValueError("Image not found or unable to load.")

# Difine windows name
window_name = ["Original Image", "3x3 Average Image", "10x10 Average Image", "20x20 Average Image"]

# create resizable windows for displaying images
for name in window_name:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 600, 600)

# Apply spatial averaging with different kernel sizes
average_3x3 = cv2.blur(img, (3, 3))
average_10x10 = cv2.blur(img, (10, 10))
average_20x20 = cv2.blur(img, (20, 20))

# Display the images
cv2.imshow(window_name[0], img)
cv2.imshow(window_name[1], average_3x3)
cv2.imshow(window_name[2], average_10x10)
cv2.imshow(window_name[3], average_20x20)

# Wait for the user to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
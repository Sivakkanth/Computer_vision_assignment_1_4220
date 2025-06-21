########################################################################
#   Take Home Assignment 1
#   Question 3
#   Reg No: EG/2020/4220
#   Date: 2025-06-16
########################################################################

# Import required libraries
import cv2
import numpy as np

# Read the image
img = cv2.imread("image/image1.jpg")

# Check if the image is loaded successfully
if img is None:
    raise ValueError("Image not found or unable to load.")  

# Get image dimensions
height, width = img.shape[:2]
center = (width / 2, height / 2)

# Function to rotate image without cropping
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)

    # Get rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Calculate the new bounding dimensions
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_width = int((h * sin) + (w * cos))
    new_height = int((h * cos) + (w * sin))

    # Adjust the rotation matrix to move the image to the center
    M[0, 2] += (new_width / 2) - center[0]
    M[1, 2] += (new_height / 2) - center[1]

    # Rotate and return the result
    return cv2.warpAffine(image, M, (new_width, new_height))

# Rotate images by 45 and 90 degrees without cropping
rotated_image = rotate_image(img, 45)
rotated_image_90 = rotate_image(img, 90)

# Define window names
window_name = ["Original Image", "Rotated Image 45 Degrees", "Rotated Image 90 Degrees"]

# Create resizable windows for displaying images
for name in window_name:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 600, 600)

# Display the images
cv2.imshow(window_name[0], img)
cv2.imshow(window_name[1], rotated_image)
cv2.imshow(window_name[2], rotated_image_90)

# Wait for the user to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
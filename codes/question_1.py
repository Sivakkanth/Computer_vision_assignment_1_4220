########################################################################
#   Take Home Assignment 1
#   Question 1
#   Reg No: EG/2020/4220
#   Date: 2025-06-16
########################################################################

# import all necessary libraries
import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread("image/image1.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    raise ValueError("Image not found or unable to load.")

# Display the image
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image", 600, 600)
cv2.imshow("Original Image", img)

# Maximum level = 8 (i.e., 2^0 = 1 to 2^8 = 256 levels)
max_level = 8
initial_level = 3 # corresponds to 2^(8 - 3) = 32 levels

def update_intensity(level):
    if level < 0 or level > max_level:
        raise ValueError(f"Level must be between 0 and {max_level}.")
    
    # Calculate the number of intensity levels
    num_levels = 2 ** level
    step = 256 // num_levels
    
    # Reduce the number of intensity levels
    reduced_image = np.floor(img / step) * step
    reduced_image = reduced_image.astype(np.uint8)
    
    # Display the new image
    cv2.imshow("Reduced Intensity Image at Level " + str(level) + "", reduced_image)

# Create a window for the trackbar
cv2.createTrackbar("Intensity Level", "Original Image", initial_level, max_level, update_intensity)

# Initialize the display with the initial level
update_intensity(initial_level)

# Wait for the user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
########################################################################
#   Take Home Assignment 1
#   Question 4
#   Reg No: EG/2020/4220
#   Date: 2025-06-16
########################################################################

# Import required libraries
import cv2
import numpy as np

# Read the image
img = cv2.imread("image/image1.jpg", cv2.IMREAD_COLOR)

# Check if the image is loaded successfully
if img is None:
    raise ValueError("Image not found or unable to load.")

# Define block sizes to simulate reduced spatial resolution
block_sizes = [3, 5, 7]

# Function to reduce spatial resolution
def reduce_resolution(image, block_size):
    # Copy the image to avoid modifying the original
    processed_image = np.copy(image)

    # Iterate over the image in blocks
    for i in range(0, image.shape[0], block_size):
        for j in range(0, image.shape[1], block_size):
            # Define the block boundaries
            roi = image[i:i + block_size, j:j + block_size]
            

            # Ensure the block does not exceed image dimensions
            if roi.shape[0] != block_size or roi.shape[1] != block_size:
                continue

            # Calculate the average color of the block
            avg_color = np.mean(roi, axis=(0, 1), dtype=np.float32)
            
            # Assign the average color to the all pixels in the block
            processed_image[i:i + block_size, j:j + block_size] = avg_color
    return processed_image.astype(np.uint8)

# Process the image for each block size
processed_images = [reduce_resolution(img, block_size) for block_size in block_sizes]

# Display the original and processed images
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image", 600, 600)
cv2.imshow("Original Image", img)

for i, processed_image in enumerate(processed_images):
    window_name = f"Processed Image (Block Size {block_sizes[i]})"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 600, 600)
    cv2.imshow(window_name, processed_image)

# Wait for the user to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
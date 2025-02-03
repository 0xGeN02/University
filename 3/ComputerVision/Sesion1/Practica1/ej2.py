import argparse
import cv2
import numpy as np
import random

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to the input image")
ap.add_argument("-n", "--grid_size", type=int, required=True, help="number of sections (N×N)")
args = vars(ap.parse_args())

# Load the input image from disk
image = cv2.imread(args["image"])

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Could not open or find the image '{args['image']}'")
    exit()

# Get the dimensions of the image
(h, w) = image.shape[:2]

# Calculate the size of each section
section_h = h // args["grid_size"]
section_w = w // args["grid_size"]

# Create an empty image to store the result
result = np.zeros_like(image)

# Loop over the grid
for i in range(args["grid_size"]):
    for j in range(args["grid_size"]):
        # Extract the section
        section = image[i * section_h:(i + 1) * section_h, j * section_w:(j + 1) * section_w]

        # Rotate the section by a random angle
        angle = random.randint(0, 360)
        M = cv2.getRotationMatrix2D((section_w // 2, section_h // 2), angle, 1.0)
        rotated_section = cv2.warpAffine(section, M, (section_w, section_h))

        # Place the rotated section back into the result image
        result[i * section_h:(i + 1) * section_h, j * section_w:(j + 1) * section_w] = rotated_section

# Display the original and resulting images
cv2.imshow("Original", image)
cv2.imshow("Result", result)
cv2.waitKey(0)

# Save the resulting image
output_path = r"C:\Users\manue\University\3\ComputerVision\Sesion1\Practica1\ej2_result.png"
cv2.imwrite(output_path, result)
print(f"Resulting image saved as '{output_path}'")


# How to use
# python ej2.py -i "path/to/your/image.png" -n 4

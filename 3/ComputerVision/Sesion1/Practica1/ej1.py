import argparse
import cv2
import numpy as np

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to the input image")
ap.add_argument("-c", "--color", type=str, required=True, choices=["red", "green", "blue"], help="color to keep")
args = vars(ap.parse_args())

# Load the input image from disk
image = cv2.imread(args["image"])

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Could not open or find the image '{args['image']}'")
    exit()

# Create a copy of the image to modify
result = image.copy()

# Set the channels to 0 based on the selected color
if args["color"] == "red":
    result[:, :, 0] = 0  # Set blue channel to 0
    result[:, :, 1] = 0  # Set green channel to 0
elif args["color"] == "green":
    result[:, :, 0] = 0  # Set blue channel to 0
    result[:, :, 2] = 0  # Set red channel to 0
elif args["color"] == "blue":
    result[:, :, 1] = 0  # Set green channel to 0
    result[:, :, 2] = 0  # Set red channel to 0

# Display the original and resulting images
cv2.imshow("Original", image)
cv2.imshow("Result", result)
cv2.waitKey(0)

# Save the resulting image
output_path = r"3/ComputerVision/Sesion1/Practica1/ej1_result.png"
cv2.imwrite(output_path, result)
print(f"Resulting image saved as '{output_path}'")

# How to use
# python ej1.py -i "path/to/your/image.png" -c "red"
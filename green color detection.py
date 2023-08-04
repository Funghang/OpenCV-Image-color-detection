import cv2
import numpy as np

image = cv2.imread("D:\\picfolder\\citizenship_data\\New_Data\\rubickscube.jpg", 1)

# Converts images from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining range of green color that we want to detect in the HSV color space
lower_green = np.array([40, 50, 50])  # Adjust the lower bounds for green
upper_green = np.array([80, 255, 255])  # Adjust the upper bounds for green

# This creates a mask of green colored regions
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Use bitwise AND operation to extract the green colored regions from the original image
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('Mask', mask)
cv2.imshow('Green Color Detection', result)
cv2.waitKey(0)

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()


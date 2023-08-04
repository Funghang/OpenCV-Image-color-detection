import cv2
import numpy as np

image = cv2.imread("D:\\picfolder\\citizenship_data\\New_Data\\rubickscube.jpg", 1)

# Converts images from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for red color in HSV
lower_red1 = np.array([0, 255, 255])    # Lower bound for first segment of red
upper_red1 = np.array([10, 255, 255])  # Upper bound for first segment of red

lower_red2 = np.array([150, 50, 50])  # Lower bound for second segment of red
upper_red2 = np.array([179, 255, 255])  # Upper bound for second segment of red

# Create masks for both segments of red
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# Combine the masks using bitwise OR operation
final_mask = cv2.bitwise_or(mask1, mask2)

# Use bitwise AND operation to extract the red colored regions from the original image
result = cv2.bitwise_and(image, image, mask=final_mask)

cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('Mask 1', mask1)
cv2.imshow('Mask 2', mask2)
cv2.imshow('Final Mask', final_mask)
cv2.imshow('Red Color Detection', result)
cv2.waitKey(0)

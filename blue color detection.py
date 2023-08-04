#Blue color detection using OpenCV
import cv2
import numpy as np

image = cv2.imread("D:\\picfolder\\citizenship_data\\New_Data\\rubickscube.jpg",1)
#Converts images from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining range of bluecolor that we want to detect in the HSV color space
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

#This creates a mask of blue coloured 
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

#Use bitwise AND operation to extract the colored regions from the original image
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('hsv_image', hsv_image  )
cv2.imshow('Mask', mask)
cv2.imshow('Blue Color Detection', result)
cv2.waitKey(0)

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

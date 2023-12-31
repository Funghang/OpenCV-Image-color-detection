# OpenCV-Image-color-detection

The purpose of the above code is to perform color detection using OpenCV, a popular computer vision library in Python. The code reads an image from a file, converts it from the default BGR color space to the HSV (Hue, Saturation, Value) color space, and then creates a mask to detect color regions in the image. The codes are written to detect blue, green and red colour region of the image.



# Here's a brief description of the code and its use:

# 1. Import Libraries
The code starts by importing the required libraries, including cv2 (OpenCV) for image processing and numpy for numerical operations.

```import cv2```

```import numpy as np```


# 2. Read the Image

The image is read from the file path specified in the cv2.imread() function. The 1 argument specifies that the image should be read in color mode (BGR).

```image = cv2.imread("full_image_path\\image_name.jpg",1) ```

In our code we have read the image of Rubicks cube, which is shown in fig below:
```image = cv2.imread("D:\\picfolder\\citizenship_data\\New_Data\\rubickscube.jpg",1)```

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/rubickscube.png) 

# 3. Convert BGR to HSV
The image is then converted from the default BGR color space to the HSV color space using cv2.cvtColor() function. HSV is often used in color detection tasks because it separates the color information into three components - Hue, Saturation, and Value.

```hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) ```

Also lets display the hsv_image

```cv2.imshow('hsv_image', hsv_image  )```

This is the picture of converted hsv_image.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/hsv%20image.png)
            
# 4. Define Blue Color Range
The lower and upper bounds of the blue color are defined in HSV color space. The lower_blue and upper_blue arrays represent the minimum and maximum values of Hue, Saturation, and Value for detecting the blue color.

```lower_blue = np.array([100, 50, 50])```

```upper_blue = np.array([130, 255, 255])```

# 5. Create the Mask
cv2.inRange() function creates a binary mask that identifies pixels within the specified HSV range. The mask will have a value of 1 (white) for the pixels that fall within the blue color range, and 0 (black) for the pixels outside the range.

```mask = cv2.inRange(hsv_image, lower_blue, upper_blue)```
Also lets display the mask

```cv2.imshow('mask image', mask)```

This is the picture of mask.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/mask%20image.png)

# 6. Extract Blue Regions
The original image is combined with the mask using cv2.bitwise_and() function. This operation extracts the blue regions from the original image by setting all non-blue pixels to black (0,0,0).
```result = cv2.bitwise_and(image, image, mask=mask)```

# 7. Display The Blue Region Of Images
The code uses cv2.imshow() to display the final result with only the blue regions visible.
```cv2.imshow('Blue Color Detection', result)```

This is the final result which shows the blue region of the image.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/blue%20image.png)

 In this way we can detect the blue color region from the image. Similarly, we can perform the same operation for detecting green region in the image. But in case of green region the upper and lower bound of the green color needs to be modified as:

```lower_green = np.array([40, 50, 50])```

```upper_green = np.array([80, 255, 255])```

With the changes in upper and lower bound for green color, the above code detects the green region of the image and is displayed as: 

```cv2.imshow('Green Color Detection', result)```

This is the final result after detecting the green region of the image.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/green%20image.png)








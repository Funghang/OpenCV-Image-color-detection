# OpenCV-Image-color-detection

The purpose of the above code is to perform color detection using OpenCV, a popular computer vision library in Python. The code reads an image from a file, converts it from the default BGR color space to the HSV (Hue, Saturation, Value) color space, and then creates a mask to detect color regions in the image. The codes are written to detect blue, green and red colour region of the image.



# Here's a brief description of the code and its use:

# 1. Importing Libraries:
The code starts by importing the required libraries, including cv2 (OpenCV) for image processing and numpy for numerical operations.

```import cv2```

```import numpy as np```


# 2.Reading the Image:

The image is read from the file path specified in the cv2.imread() function. The 1 argument specifies that the image should be read in color mode (BGR).

```image = cv2.imread("full_image_path\\image_name.jpg",1) ```

In our code we have read the image of Rubicks cube, which is shown in fig below:

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/rubickscube.png) fig1

# 3. Converting BGR to HSV:
The image is then converted from the default BGR color space to the HSV color space using cv2.cvtColor() function. HSV is often used in color detection tasks because it separates the color information into three components - Hue, Saturation, and Value.

```hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) ```

Also lets display the hsv_image

```cv2.imshow('hsv_image', hsv_image  )```

This is the picture of converted hsv_image.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/hsv%20image.png)
fig2

# 4. Defining Blue Color Range:
The lower and upper bounds of the blue color are defined in HSV color space. The lower_blue and upper_blue arrays represent the minimum and maximum values of Hue, Saturation, and Value for detecting the blue color.

```lower_blue = np.array([100, 50, 50])```
```upper_blue = np.array([130, 255, 255])```

# 5. Creating the Mask:
cv2.inRange() function creates a binary mask that identifies pixels within the specified HSV range. The mask will have a value of 1 (white) for the pixels that fall within the blue color range, and 0 (black) for the pixels outside the range.

```mask = cv2.inRange(hsv_image, lower_blue, upper_blue)```
Also lets display the mask

```cv2.imshow('mask image', mask  )```

This is the picture of mask.

![Alt Text](https://github.com/Funghang/OpenCV-Image-color-detection/blob/main/mask%20image.png)
fig2







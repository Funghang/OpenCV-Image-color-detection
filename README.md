# OpenCV-Image-color-detection

The purpose of the above code is to perform color detection using OpenCV, a popular computer vision library in Python. The code reads an image from a file, converts it from the default BGR color space to the HSV (Hue, Saturation, Value) color space, and then creates a mask to detect color regions in the image. The codes are written to detect blue, green and red colour region.



# Here's a brief description of the code and its use:

Importing Libraries: The code starts by importing the required libraries, including cv2 (OpenCV) for image processing and numpy for numerical operations.

```import cv2```

```import numpy as np```


Reading the Image: The image is read from the file path specified in the cv2.imread() function. The 1 argument specifies that the image should be read in color mode (BGR).

```image = cv2.imread("full_image_path\\image_name.jpg",1) ```

In our code we have read the image of Rubicks cube, which is shown in fig below:

![Alt Text](https://github.com/Funghang/OpenCV/raw/main/rubickscube.jpg)

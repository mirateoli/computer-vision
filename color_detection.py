import cv2
import numpy as np
import matplotlib as plt

# load in image
img = cv2.imread('red_ball.jpg')
# convert from BGR to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define color range we are looking for based on color we expect/want
lower_range = (0, 50, 50)       # lower range of red in HSV
upper_range = (10, 255, 255)    # upper range of red in HSV

# extract pixels in the chosen color range
mask = cv2.inRange(hsv_img, lower_range, upper_range)

# apply the mask created to the original "hsv_img" 
color_image = cv2.bitwise_and(img, img, mask=mask)

# display the color image
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.imshow("HSV Image", hsv_img)
cv2.waitKey(0)
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt

# Open the image
img = cv2.imread("penguin.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny Edge Dection
edged = cv2.Canny(blurred, 30, 100, 3, L2gradient=True)

# find the contours in the edged image
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_copy = img.copy()
# draw the contours on a copy of the original image
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
print(len(contours), "objects were found in this image.")

cv2.imshow("Edged image", edged)
cv2.imshow("contours", image_copy)
cv2.imshow("Original image", img)
cv2.imshow("Edged image", edged)
cv2.waitKey(0)
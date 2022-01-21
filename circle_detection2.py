import cv2
import numpy as np
import time

# openCV version 4.4.0
# start_time = time.time()
original = cv2.imread('sensed/006.jpg', cv2.IMREAD_COLOR)
resize = original.copy()

dimensions = resize.shape
height = resize.shape[0]
width = resize.shape[1]

if height > 1000 or width > 1000:
    # Percent value that the image is resized
    scale_percent = 50
    # Calculates the resized dimensions using the original dimension
    width = int(resize.shape[1] * scale_percent / 100)
    height = int(resize.shape[0] * scale_percent / 100)
    # Desired resizing parts of the image
    desired_size = (width, height)
    # Fully resized image
    img = cv2.resize(resize, desired_size)
else:
    img = resize

# Circle detection code

# Converts to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Hough transforms on the image
detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.1, 100, param1=420, param2=10)
# Draws circles that are detected
if detected_circles is not None:
    # Convert the circle parameters
    detected_circles = np.uint16(np.around(detected_circles))
    x, y, radius = int(detected_circles[0][0][0]), int(detected_circles[0][0][1]), int(detected_circles[0][0][2])
    center = (x, y)
    # Draws the circumference of the detected circle
    cv2.circle(img, center, 1, (0, 255, 0), 1)
    # Draws a small circle to show the center of the detected circle
    cv2.circle(img, center, radius, (0, 0, 255), 2)
height = img.shape[0]
width = img.shape[1]
# Displays the outcome of circle detection
cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print("--- %s seconds ---" % (time.time() - start_time))

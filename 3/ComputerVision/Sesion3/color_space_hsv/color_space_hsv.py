# Detect green balls from the input image. 
import numpy as np
import cv2 

while True:
    # Image read
    frame = cv2.imread('course.PNG') 

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([57, 49, 50])
    upper_blue = np.array([85, 250, 250])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    # This is going to open three windows 
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(1)
    # If the pressed key is escape key
    if k == 27:
        break

cv2.destroyAllWindows()
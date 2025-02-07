import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def goodCornerDetection():
    root = os.getcwd()
    imgPath = os.path.join(root, 'objects.png')
    img = cv.imread(imgPath)
    imgRGB= cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    maxCorners = 200
    quality = 0.01
    minDistance = 20

    corners = cv.goodFeaturesToTrack(imgGray, maxCorners, quality, minDistance)

    for corner in corners:
        x = int(corner[0][0])
        y = int(corner[0][1])
        cv.circle(imgRGB, (x, y), 3, (255, 0, 0), -1)
    
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    goodCornerDetection()
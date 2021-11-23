import os

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def findShapes():
    # Get the image from the drawing
    image = cv.imread(os.path.join(os.path.dirname(__file__), 'Drawings/savedImage.png'))

    # Convert the image to grayscale
    grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Edge Detection
    edges = cv.Canny(grayscale, 50, 100)

    # Now get the lines using houghlinesP
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 60, np.array([]), 50, 5)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)

    plt.imshow(image)
    plt.show()

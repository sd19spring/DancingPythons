import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os


# capture frames using cap
cap = cv2.VideoCapture(0)

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)

    cv2.imshow('In Py Feelings',edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

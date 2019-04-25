#things to import
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os

#initializing colors
white = [255,255,255]
black = [0,0,0]

# capture frames using cap
cap = cv2.VideoCapture(0)
art = cv2.imread('myart.png')

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,50,120)

    #here edges is converted to have the same number of channels
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

    display = cv2.add(art,edges)
    # Display edges image in a frame
    cv2.imshow('Dancing Pythons',edges)
    cv2.imshow('art',art)
    cv2.imshow('Both',display)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()

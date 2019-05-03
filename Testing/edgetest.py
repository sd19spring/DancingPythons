import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os

# capture frames using cap
cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 360)
art = cv2.VideoCapture('art_test.mp4')

counter = 0;
while(1):
    counter +=1
    # reads frames from a camera
    ret, frame = cap.read()
    ret2, art_frame = art.read()
    print(art_frame.shape)
    print(frame.shape)
    # finds edges in the input frame
    edges = cv2.Canny(frame,50,220)
    #here edges is converted to have the same number of channels
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

    display = cv2.add(art_frame,edges)
    # Display edges image in a frame
    cv2.imshow('Dancing Pythons',edges)
    cv2.imshow('art',art)
    cv2.imshow('Both',display)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:

        break

# Close the window
#print(counter)
cap.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()

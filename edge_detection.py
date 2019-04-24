#things to import
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os

#initializing colors
white = [255,255,255]
black = [0,0,0]
outline_color = [250,40,2]

# capture frames using cap
cap = cv2.VideoCapture(0)
art = cv2.imread('myart_sized.png')

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)

    #here every black pixel is converted to another constant color
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)

    #changing the trace color to black
    edges[np.all(edges == [255,255,255], axis=2)] = white
    whites = edges[np.all(edges == [255,255,255], axis=2)]
    outline = np.all(edges == whites[0][0], axis=2)
    edges[outline] = outline_color

    '''#changing the backgroung color to white
    edges[np.all(edges == [0,0,255], axis=2)] = black
    backgound = edges[0][0]
    backgound = np.all(edges == backgound, axis=2)
    edges[backgound] = black'''



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

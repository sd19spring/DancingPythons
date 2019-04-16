'''import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw


# capture frames using cap
cap = cv2.VideoCapture(0)
art = cv2.imread('test.png',0)

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)


    # Display edges in a frame
    cv2.imshow('In Py Feelings',edges)
    cv2.imshow('art',art)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()'''



'''Here is a test'''

import cv2
import numpy as np

# create an overlay image. You can use any image
background = cv2.imread('test.png')
# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.4
while True:
    # read the frame
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)

    # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
    added_image = cv2.addWeighted(edges[0:100,0:100],alpha,background[0:100,0:100],1-alpha,0)
    # Change the region with the result
    edges[150:200,150:200] = added_image
    # For displaying current value of alpha(weights)

    cv2.imshow('a',frame)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()

#things to import
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os


# capture frames using cap
cap = cv2.VideoCapture(0)
art = cv2.imread('test.png')

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)


    #turns the frame of edges into an image
    #at this point the image is a black and white where white pixels are edges
    cv2.imwrite("edges.jpg", edges)
    edges = cv2.imread("edges.jpg")

    #here every black pixel is converted to another constant color
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    '''edges[np.all(edges == [0,0,255], axis=2)] = [0, 0, 0]
    bg_color = edges[0][0]
    mask = np.all(edges == bg_color, axis=2)
    edges[mask] = [0,0,150]'''

    #here we are trying to test converting black pixels to
    #a specific color that depends on its location and the color
    #of the same pixel in the generated art
    '''for x in range(100):
        for y in range(200):
            pixel = art[x,y]
            edges[mask] = pixel'''

    #here we are trying to transfer every white pixel to the art; the opposite of other approaches
    positions = []
    for x in range(100):
        for y in range(200):
            if edges.getpixel((x,y)) == [255,255,255]:
                positions[y] = (x,y)

    for (x,y) in positions:
        

    # Display edges image in a frame
    cv2.imshow('In Py Feelings',edges)
    cv2.imshow('art',art)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    #remove each frame that was converted to an image to
    os.remove("edges.jpg")

# Close the window
cap.release()
os.remove("edges.jpg")

# De-allocate any associated memory usage
cv2.destroyAllWindows()



#past testing; please ignore
'''
import cv2
import numpy as np

# create an overlay image. You can use any image
background = cv2.imread('test.png')
background = background[0:100,0:200]
# Open the camera
cap = cv2.VideoCapture(0)
# Set initial value of weights
alpha = 0.4
gamma = 1-0.4
while True:
    # read the frame
    ret, frame = cap.read()

    # finds edges in the input frame and
    edges = cv2.Canny(frame,100,200)

    # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
    added_image = cv2.addWeighted(edges,alpha,background,gamma,0)
    # Change the region with the result
    edges = added_image
    # For displaying current value of alpha(weights)

    cv2.imshow('a',frame)
    k = cv2.waitKey(10)
    # Press q to break
    if k == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
'''

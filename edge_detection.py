import numpy as np
import cv2



# capture frames using cap
cap = cv2.VideoCapture(0)

while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting to black and white traces?
    '''hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # Display an original image
    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)'''

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame,100,200)

    for edge in edges:
        if edge == [0,0,0]:
            

    # Display edges in a frame
    cv2.imshow('Edges',edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

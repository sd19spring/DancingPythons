import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os

art = Image.open('myart.png')
edges = Image.open('edges.jpg')
edges = edges.resize((350,350))

x_size = edges.size[0]
y_size = edges.size[1]

'''print(edges.size)
print(art.size)'''

'''edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
edges[np.all(edges == [0,0,255], axis=2)] = [0, 0, 0]
bg_color = edges[0][0]
mask = np.all(edges == bg_color, axis=2)
edges[mask] = [0,0,150]'''


#test here
for x in range(x_size):
    for y in range(y_size):
        xy = (x,y)
        pixel = art.getpixel(xy)
        if edges.getpixel(xy) == (0,0,0):
            edges.putpixel(xy,pixel)

edges.save("edges4.png")

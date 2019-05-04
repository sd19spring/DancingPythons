#things to import
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from matplotlib import pyplot as py
import os

def get_edges(frame):
    edges = cv2.Canny(frame,50,220)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    return edges

def get_new_art(index):
    location = 'images/'+ str(index) + '.png'
    art = cv2.imread(location)
    return art

def compile(art,edges):
    display = cv2.add(art,edges)
    return display

def reset_index():
    return 0

def main(duration):
    cap = cv2.VideoCapture(0)
    index = 0
    for tic in range(duration):
        ret, frame = cap.read()

        edges = get_edges(frame)

        index += 1
        art = get_new_art(index)
        if index == 4:
            index = reset_index()


        display = compile(art,edges)
        cv2.imshow('Dancing Pythons',display)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(duration)

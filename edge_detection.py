'''
edge_detection.py creates the final display of edges on art. It parses through
the correct folder of images depending on the mood and adds it to edges detected
by Canny Edge Detection to create what you see when you run main.pyself. Because
this is where everything comes together it is also where spotify plays the song
you are dancing to. In order for it to play, you must have the spotify app open
on your device.
'''

#libraries needed
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
import spotipy
import timeit
import music_to_mood

def get_edges(frame):
    edges = cv2.Canny(frame,100,270)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    return edges

def get_new_art(mood, index,size):
    location = 'images/'+ mood[0]+'_'+mood[1] +'/' +str(index) + '.png'
    art = cv2.imread(location)
    art = cv2.resize(art, (size[0], size[1]), interpolation = cv2.INTER_LINEAR)
    return art

def compile(art,edges):
    display = cv2.add(art,edges)
    return display

def reset_index():
    return 0

def play_song(uri):
    music_to_mood.sp.start_playback(uris = [uri])

def main(mood, duration,uri,size = [1922,1080]):
    cap = cv2.VideoCapture(0)
    cap.set(3,size[0])
    cap.set(4,size[1])

    play_song(uri)

    index = 0
    t = timeit.Timer()
    while t.timeit()<=duration:
        ret, frame = cap.read()
        edges = get_edges(frame)
        edges = cv2.resize(edges, (size[0], size[1]), interpolation = cv2.INTER_AREA)

        art = get_new_art(mood, index,size)
        if index == 19:
            index = reset_index()
        index += 1

        display = compile(art,edges)

        cv2.imshow('Dancing Pythons',display)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(mood,duration,uri)

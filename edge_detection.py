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
import time
import music_to_mood

def get_edges(frame):
    '''
    Uses Open CV's Canny Edge Detection to to obtain edges from camera frame.
    Returns the edges in RGB form so that they can be added to the art later.
    '''
    edges = cv2.Canny(frame,100,270)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    return edges

def get_new_art(mood, index,size):
    '''
    Returns the correct art image in the right mood folder, and in the right
    sequence. The image is also resized to fit the fullscreen frame
    '''
    location = 'images/'+ mood[0]+'_'+mood[1] +'/' +str(index) + '.png'
    art = cv2.imread(location)
    art = cv2.resize(art, (size[0], size[1]), interpolation = cv2.INTER_LINEAR)
    return art

def compile(art,edges):
    '''
    Compiles the ard and edges together and returns the final display.
    '''
    display = cv2.add(art,edges)
    return display

def reset_index():
    '''
    Resets the index so that the art is looped through for the duration of the song.
    '''
    return 0

def play_song(uri):
    '''
    Plays the song as soon as the edge detection begins
    '''
    music_to_mood.sp.start_playback(uris = [uri])

def main(mood, duration,uri,size = [1922,1080]):
    '''
    Calls all helper functions to initialize the camera, put together art, display, and play
    '''
    cap = cv2.VideoCapture(0)
    cap.set(3,size[0])
    cap.set(4,size[1])

    play_song(uri)

    index = 0
    start = time.time()
    elapsed = 0
    while  elapsed<=duration:
        elapsed = time.time() - start
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

'''
This is the main script that brings everything. To run and use the program run main.py.
But, make sure you have already run set_up.py once before this so you have folders for
each mood category.

In order for this program to run you in need to install numpy, open cv, and python
image library, and a few others. Please see the README for help on how to install
the neccessary packages.
'''
import edge_detection
import music_to_mood
import set_up
import os

def main():
    print('Welcome to Dancing Pythons! \nIf this is your first time, be sure that you ran set_up.py before running main.py. \nOtherwise, make sure your Spotify App is running on your device and have fun!')
    mood,duration,uri = music_to_mood.main()
    print(duration)
    edge_detection.main(mood,duration,uri)

if __name__ == '__main__':
    main()

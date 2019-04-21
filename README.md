# Dancing Pythons
Create an entertaining and stimulating visual at your next party or hangout! Using your computer's webcam, Dancing Pythons will create silhouettes of you and your friends as you dance about on a colorful background. By inputting a Spotify song, Dancing Pythons is able to select a background that matches the mood - slow, wavy blues might greet you as you sway back and forth to Adele while flashy reds can psyche you up for a punk song! 

## Getting Started
#Prerequisites
Be sure that you have a working webcam connected to your computer.
#Installing
Install OpenCV, Spotipy, and PIL by running the following in the command line of your machine:
```
pip install opencv
pip install spotipy
pip install pil
```
# Physical Space and Placement
Dancing Pythons uses edge detection in order to draw the silhouettes of those dancing in front of the webcam onto the colorful background. In order to better highlight you and your friends dancing as opposed to the exterior environment, set up the webcam to face a blank background with as little variation in coloring and items in the view as possible. If possible, set up the webcam at about shoulder height.

## Deployment
Run main.py in order to initialize the Dancing Pythons visualizer.
To start, music_to_mood.py will be called in order to select a song and determine its lenght, mood, and tempy. You will be asked to input a track title in order to search for a song through Spotify's api. Be sure to check your spelling in order to find your song quickly!
Once the song is selected, mood_to_art.py will be called to randomly generate a colorful background according to the song's features.
After the background is generated, edge_detection.py will be called to draw the edges of what is detected on the webcam onto the colorful background. 

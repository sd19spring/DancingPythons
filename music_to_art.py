import recursive_art as art

art.generate_art('test.png')

import spotipy

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out

def get_mood(song):
    q = song
    mood = GET https://api.spotify.com/v1/audio-analysis/{q}

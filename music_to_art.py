import recursive_art as art

art.generate_art('test.png')

import spotipy

client_id = '2c49178b39bc423dbb44f1ce220c12bb' //client id
client_secret = 'ecb09ffa5ffe46d2844e1bd07c75659e' // secret id
redirect_uri = 'REDIRECT_URI' //

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out

def get_mood(song):
    q = song
    mood = GET https://api.spotify.com/v1/audio-analysis/{q}

def get_colors(mood):
    moods = {'chill': [[152,222,201],[250,182,211],[246,246,160],[153,204,255]],
            'angry': [[111,121,131],[21,5,165],[165,58,5],[14,122,17]],
            'sad': [[121,111,111]]
            #add additional moods here
            }
    return moods[mood]

# shows audio analysis for the given track

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials('2c49178b39bc423dbb44f1ce220c12bb', 'ecb09ffa5ffe46d2844e1bd07c75659e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    tid = 'spotify:track:4TTV7EcfroSLWzXRY6gLv6'

start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(sp.audio_features(tid))
#print(json.dumps(analysis, indent=4))
#print ("analysis retrieved in %.2f seconds" % (delta,))

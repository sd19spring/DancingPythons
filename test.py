# shows audio analysis for the given track

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


client_credentials_manager = SpotifyClientCredentials('2c49178b39bc423dbb44f1ce220c12bb', 'ecb09ffa5ffe46d2844e1bd07c75659e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def test_confirmation(confirmation):
    if confirmation == 'Y':
        uri = results['tracks']['items'][1]['uri']
        break
    elif confirmation == 'N':
        print('Noooo')
        break
    else:
        print('Please answer the question again. Type Y or N and then hit enter.')
        confirmation = input('Is the song ' + results['tracks']['items'][1]['name'] + ' by ' + results['tracks']['items'][1]['artists'][0]['name'] + '? Y/N \n')
        test_confirmation(confirmation)

search_input = '"' + input('What song do you want to dance to? Please enter the track title. \n') + '"'
results = sp.search(q=search_input, limit=3, type='track')
results['tracks']['items'][1]['artists'][0]['name']
confirmation = input('Is the song ' + results['tracks']['items'][1]['name'] + ' by ' + results['tracks']['items'][1]['artists'][0]['name'] + '? Y/N \n')
test_confirmation(confirmation)
print(uri)
#tid = 'spotify:track:4bHsxqR3GMrXTxEPLuK5ue'
#print(sp.track(tid))
#start = time.time()
#analysis = sp.audio_analysis(tid)
#delta = time.time() - start
#print(sp.audio_features(tid))
#print(json.dumps(analysis, indent=4))
#print ("analysis retrieved in %.2f seconds" % (delta,))

'''
music_to_mood.py takes in a song and uses Spotify's API to output a mood that
falls in one of four categories: 1) negative with high energy 2) negative with
low energy 3) positive with high energy 4) positive with low energy. The mood
depends on the valance and energy of the song. This script also plays the given
song.
'''

from __future__ import print_function
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import spotipy.util as util
import sys

def setup_credentials():
    """
    sets up all the credentials needed for data and to pause/play and returns it
    """
    if 'sp' not in globals():
        scopes = 'user-modify-playback-state'
        token = util.prompt_for_user_token( 'dpatel3836',
                                            scopes,
                                            client_id = '2c49178b39bc423dbb44f1ce220c12bb',
                                            client_secret = my_secret_id, '25cbe09bd4a8494cb525f7b53c1b726c'
                                            redirect_uri = 'http://example.com/callback/')
        sp = spotipy.Spotify(auth=token)
    return sp
sp = setup_credentials()

class SearchError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

def test_confirmation(confirmation, results):
    if confirmation == 'Y':
        return results['tracks']['items'][0]['uri']
    elif confirmation == 'N':
        if len(results['tracks']['items']) > 1:
            confirmation2 = input('Is the song ' + results['tracks']['items'][1]['name'] + ' by ' + results['tracks']['items'][1]['artists'][0]['name'] + '? Y/N \n')
            return test_confirmation2(confirmation2, results)
        else:
            raise SearchError('Your search only yielded that 1 result. Please rerun the program and try again. Check your spelling!')
    else:
        print('Please answer the question again. Type Y or N and then hit enter.')
        confirmation = input('Is the song ' + results['tracks']['items'][0]['name'] + ' by ' + results['tracks']['items'][0]['artists'][0]['name'] + '? Y/N \n')
        test_confirmation(confirmation, results)

def test_confirmation2(confirmation2, results):
    if confirmation2 == 'Y':
        return results['tracks']['items'][1]['uri']
    elif confirmation2 == 'N':
        if len(results['tracks']['items']) > 2:
            confirmation3 = input('Is the song ' + results['tracks']['items'][2]['name'] + ' by ' + results['tracks']['items'][2]['artists'][0]['name'] + '? Y/N \n')
            return test_confirmation3(confirmation3, results)
        else:
            raise SearchError('Your search only yielded those 2 results. Please rerun the program and try again. Check your spelling!')
    else:
        print('Please answer the question again. Type Y or N and then hit enter.')
        confirmation2 = input('Is the song ' + results['tracks']['items'][1]['name'] + ' by ' + results['tracks']['items'][1]['artists'][0]['name'] + '? Y/N \n')
        test_confirmation2(confirmation2, results)

def test_confirmation3(confirmation3, results):
    if confirmation3 == 'Y':
        return results['tracks']['items'][2]['uri']
    elif confirmation3 == 'N':
        sys.tracebacklimit = 0
        raise SearchError('Your search did not yield the song you were looking for in the top 3 results. Please rerun the program and try again. Check your spelling!')
    else:
        print('Please answer the question again. Type Y or N and then hit enter.')
        confirmation3 = input('Is the song ' + results['tracks']['items'][2]['name'] + ' by ' + results['tracks']['items'][2]['artists'][0]['name'] + '? Y/N \n')
        test_confirmation3(confirmation3, results)

def main():
    search_input = '' + input('What song do you want to dance to? Please enter the track title. \n') + '"'
    results = sp.search(q=search_input, limit=3, type='track')
    if len(results['tracks']['items']) == 0:
        sys.tracebacklimit = 0
        raise SearchError('Your search did not yield any matching songs. Please rerun the program and try again. Check your spelling!')
    confirmation = input('Is the song ' + results['tracks']['items'][0]['name'] + ' by ' + results['tracks']['items'][0]['artists'][0]['name'] + '? Y/N \n')
    uri = test_confirmation(confirmation, results)
    track_analysis = sp.audio_features(uri)

    if track_analysis[0]['valence'] <= 0.5 and track_analysis[0]['energy'] <= 0.5:
        mood = ['negative', 'low energy']
    elif track_analysis[0]['valence'] <= 0.5 and track_analysis[0]['energy'] > 0.5:
        mood = ['negative', 'high energy']
    elif track_analysis[0]['valence'] > 0.5 and track_analysis[0]['energy'] <= 0.5:
        mood = ['positive', 'low energy']
    elif track_analysis[0]['valence'] > 0.5 and track_analysis[0]['energy'] > 0.5:
        mood = ['positive', 'high energy']
    dur = track_analysis[0]['duration_ms']
    return mood,dur,uri

if __name__ == '__main__':
    main()

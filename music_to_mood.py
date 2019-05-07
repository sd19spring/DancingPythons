'''
music_to_mood.py takes in a song and uses Spotify's API to output a mood that
falls in one of four categories: 1) negative with high energy 2) negative with
low energy 3) positive with high energy 4) positive with low energy. The mood
depends on the valance and energy of the song. This script also plays the given
song.
'''
#libraries needed
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import sys
from config import *

def setup_credentials():
    '''
    sets up all the credentials needed for data and to pause/play and returns it
    '''
    if 'sp' not in globals():
        scopes = 'user-modify-playback-state'
        token = util.prompt_for_user_token(my_username,
                                            scopes,
                                            client_id = my_client_id,
                                            client_secret = my_client_secret,
                                            redirect_uri = 'http://example.com/callback/')
        sp = spotipy.Spotify(auth=token)
    return sp

sp = setup_credentials()

def get_mood(valance, energy):
    '''
    Takes the valance and energy of a song and retuns the mood categogy
    '''
    mood = ['','']
    if valance > 0.5:
        mood[0] = 'positive'
    else:
        mood[0] = 'negative'

    if energy > 0.5:
        mood[1] = 'high energy'
    else:
        mood[1] = 'low energy'
    return mood

def get_song():
    '''
    Get's the song from the user through the terminal and checks for verification 3 times before giving up
    '''
    song_choice = input('What song would you like to dance to?\n')
    result = sp.search(q = song_choice,type = 'track',limit = 3)
    top_three = [result['tracks']['items'][0],result['tracks']['items'][1],result['tracks']['items'][2]]

    for track in top_three:
        verification = check(track)
        if verification == 'Y' or verification == 'y':
            return track

    print('Your search did not yield the song you were looking for in the top 3 results. Please run main.py again. Check your spelling!')
    sys.exit()

def check(track):
    '''
    Asks the user if the song found is the one they were looking for
    '''
    title = track['name']
    artist = track['artists'][0]['name']
    verification = input('Is the song ' + title + ' by ' + artist + '? Y/N \n')
    return verification

def analyze(track):
    '''
    analyzes the correct track and returns the uri,duration,valance, and energy
    '''
    uri = track['uri']
    duration = track['duration_ms']

    valence = sp.audio_features(uri)[0]['valence']
    energy = sp.audio_features(uri)[0]['energy']

    return uri,valence,energy,duration

def main():
    '''
    Finds the correct song, then its attributes, then returns the mood and duration
    with the help of helper functions
    '''
    correct_song = get_song()
    uri,valence,energy,duration = analyze(correct_song)
    mood = get_mood(valence,energy)
    return mood,duration,uri

if __name__ == '__main__':
    main()

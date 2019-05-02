#import other code
import edge_detection
import music_to_mood
import mood_to_art
import os

def main():
    mood,duration = music_to_mood.main()
    art = mood_to_art.main()
    edge_detection.main(duration)
    for i in range(duration/2):
        location = 'images/'+ str(i) + '.png'
        os.remove(location)

if __name__ == '__main__':
    main()

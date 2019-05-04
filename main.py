#import other code
import edge_detection
import music_to_mood
import mood_to_art
import os

def main():
    mood,duration = music_to_mood.main()
    #art = mood_to_art.main(mood)
    edge_detection.main(mood,duration)
    for i in range(5):
        location = 'images/'+ mood[0]+'_'+mood[1] +'/' +str(i) + '.png'
        os.remove(location)

if __name__ == '__main__':
    main()

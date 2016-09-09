# from pydub import AudioSegment
# from pydub import playback
# import sys
# import os


# def main():
#     argv = sys.argv
#     if len(argv) < 4:
#         print "usage: python fade_play.py filename fade_in fade_out"
#         return

#     filename = argv[1]
#     fade_in = int(argv[2])
#     fade_out = int(argv[3])

#     a = AudioSegment.from_mp3(filename)
#     playback.play(a.fade_in(fade_in).fade_out(fade_out))

# main()

import pygame.mixer
import time
import sys
import os

def main():
    argv = sys.argv
    if len(argv) < 4:
        print "usage: python fade_play.py filename fade_in fade_out"
        return

    filename = argv[1]
    fade_in = int(argv[2])
    fade_out = int(argv[3])

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0)

    duration = 10.0
    fade_in = 3.0
    fade_out = 3.0


    start = time.time()
    pygame.mixer.music.stop()
    pygame.mixer.music.play(1) 

    # force playing 
    while not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(1) 
        time.sleep(0.1)

    while True:
        pos = time.time() - start
        if pos >= duration:
            break

        if pos < fade_in:
            vol = pos/fade_in
        elif pos > duration - fade_out:
            vol = (duration - pos)/fade_out
        else:
            vol = 1.0

        pygame.mixer.music.set_volume(vol)

        time.sleep(0.1)

    pygame.mixer.music.stop()



if __name__ == "__main__":
    main()

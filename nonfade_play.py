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

import time
import sys
import os
import platform

def main():
    argv = sys.argv
    if len(argv) < 2:
        print "usage: python fade_play.py filename"
        return

    filename = argv[1]

    
    if platform.system() == 'Darwin': # mac
        os.system("afplay %s" % filename)
    else:
        os.system("omxplayer %s" % filename)


if __name__ == "__main__":
    main()

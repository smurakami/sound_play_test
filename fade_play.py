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

#     a = AudioSegment.from_mp3(filename)[:10000]
#     playback.play(a.fade_in(fade_in).fade_out(fade_out))


# main()

import platform
import time
import sys
import os

def main():
    argv = sys.argv
    if len(argv) < 4:
        print "usage: python fade_play.py filename fade_in fade_out"
        return

    filename = argv[1]

    dst = filename.replace(".mp3", "_fade.wav")

    fade_in = int(argv[2]) / 1000
    fade_out = int(argv[3]) / 1000
    duration = 30

    os.system("sox %s %s fade t %d %d %d" % (filename, dst, fade_in, duration, fade_out))

    if platform.system() == 'Darwin': # mac
        os.system("afplay %s" % dst)
    else:
        os.system("omxplayer -o local --vol %d %s" % (volume, dst))


if __name__ == "__main__":
    main()

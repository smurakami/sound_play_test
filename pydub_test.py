from pydub import AudioSegment

def main():
    filename = 'data/song_0.mp3'
    a = AudioSegment.from_mp3(filename)
    a.fade_in(fade_in).fade_out(fade_out)

    # playback.play(a.fade_in(fade_in).fade_out(fade_out))
    

main()

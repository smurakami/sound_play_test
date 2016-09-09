from pydub import AudioSegment

def main():
    fade_in = 3000
    fade_out = 3000

    filename = 'data/song_0.mp3'
    a = AudioSegment.from_mp3(filename)
    b = a.fade_in(fade_in).fade_out(fade_out)

    # playback.play(a.fade_in(fade_in).fade_out(fade_out))
    # b.export("out.wav", format="wav")
    b.export("out.mp3", format="mp3")
    

main()

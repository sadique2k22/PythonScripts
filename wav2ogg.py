from pydub import AudioSegment

def wav_to_ogg(wav_file, ogg_file):
    sound = AudioSegment.from_wav(wav_file)
    sound.export(ogg_file, format="ogg")

wav_file = "output.wav"
ogg_file = "output.ogg"

wav_to_ogg(wav_file, ogg_file)

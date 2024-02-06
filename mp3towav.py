from pydub import AudioSegment

def mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

mp3_file = "input.mp3"
wav_file = "output.wav"

mp3_to_wav(mp3_file, wav_file)

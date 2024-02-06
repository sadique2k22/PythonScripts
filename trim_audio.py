from pydub import AudioSegment

def cut_audio(input_file, output_file, start_time, end_time):
    sound = AudioSegment.from_file(input_file)
    new_sound = sound[start_time:end_time]
    new_sound.export(output_file, format="wav")

input_file = "input.wav"
output_file = "output.wav"
start_time = 0  # Start time in milliseconds
end_time = 250  # End time in milliseconds (0.25 seconds)

cut_audio(input_file, output_file, start_time, end_time)

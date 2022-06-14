from pydub import AudioSegment

audio = AudioSegment.from_wav("ejemplo.wav")

audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("nuevo.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("nuevo.mp3")

print("finalizo")

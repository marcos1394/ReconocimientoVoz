import pyaudio
import wave

Frames_Per_Buffer = 3200
Format = pyaudio.paInt16
Channels = 1
Rate = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=Format,
    channels=Channels,
    rate=Rate,
    input=True,
    frames_per_buffer=Frames_Per_Buffer
)

print("Comienza la Grabación")

seconds = 5
frames = []

for i in range(0, int(Rate/Frames_Per_Buffer*seconds)):
    data = stream.read(Frames_Per_Buffer)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("ejemplo.wav", "wb")
obj.setnchannels(Channels)
obj.setsampwidth(p.get_sample_size(Format))
obj.setframerate(Rate)
obj.writeframes(b"".join(frames))
obj.close()


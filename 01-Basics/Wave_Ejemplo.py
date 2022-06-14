# formatos de archivos de audio
# .mp3: formato de compresión con perdida (quiere decir que se pierde algo de los datos)
# .flac: formato de compresión sin perdida
# .wav: formato sin comprimir

import wave

# parametros de señales de audio
# - numero de canales (mono (uno), estero(dos))
# - ancho de la muestra
# - velocidad de fotogramas / frecuencia de muestreo
# - numero de fotogramas
# - valores de los fotogramas

# con el método open abriremos un archivo con extensión .wav
# este método recibe dos parametros uno la ruta del archivo, el segundo como lo leera en este caso usaremos rb de read binary
obj = wave.open("ejemplo.wav", "rb")

print("numero de canales:", obj.getnchannels())
print("ancho de la muestra:", obj.getsampwidth())
print("velocidad de fotograma:", obj.getframerate())
print("numero de fotogramas:", obj.getnframes())
print("parametros", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)


frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

# ahora procedemos a escribir en un nuevo archivo .wav
obj_new = wave.open("ejemplo_nuevo.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()


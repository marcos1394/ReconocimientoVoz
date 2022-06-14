import sys
from api_communication import *
# subir el archivo local a ensamblador

filename = sys.argv[1]
audio_url = upload(filename)
save_transcript(audio_url, filename)

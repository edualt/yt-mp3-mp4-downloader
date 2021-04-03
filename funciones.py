import os
import subprocess
import ffmpeg

from pytube import YouTube
import pytube

def mp4(link):
    return YouTube(link).streams.first().download("/home/eduardo/Descargas/pytube")

def mp3(link):
    aud = link.streams.filter(only_audio=True).first() #Extraer solo el audio
    destino = "/home/eduardo/Descargas/pytube"
    
    out_file = aud.download(output_path=destino)
    
    base, ext= os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    
    print(link.title + "Se descargo correctamente")


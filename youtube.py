import funciones
from pytube import YouTube

print("Este es un sistema para descargar videos y musica, ingrese el link a continuacion")
link = input()

print("En que formato desea descargarlo? (mp3 o mp4)")
vid = input()


if vid == "mp4":
    video = funciones.mp4(link)
    
if vid == "mp3":
    link = YouTube(str(link))
    audio = funciones.mp3(link)

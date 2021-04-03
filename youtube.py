import funciones
from pytube import YouTube

print("Este es un sistema para descargar videos y musica, ingrese el link a continuacion")
link = input()

while True:
    if "youtube.com/watch?v=" in link:
        break
    else:
        print("hay algo mal, vuelva a ingresar el link!")
    link = input()

print("En que formato desea descargarlo? (mp3 o mp4)")
vid = input()

if vid == "mp4":
    video = funciones.mp4(link)
    
if vid == "mp3":
    link = YouTube(link)
    audio = funciones.mp3(link)

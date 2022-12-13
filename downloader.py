from moviepy.editor import *
from pytube import YouTube

link = str(input("Entre com o Link: "))
yt = YouTube(link)
print("LINK: ", link)

yt.streams.filter(abr="128kbps", progressive=False, only_audio = True).first().download(filename="audio.mp3")
#download video only
yt.streams.filter(progressive=False).get_highest_resolution().download(filename="video.mp4")

videoclip = VideoFileClip(r".\video.mp4")

audioclip = AudioFileClip("audio.mp3")

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip

videoclip.write_videofile(f"{yt.title}.mp4")
#videoclip.write_videofile("videoFinal.mp4")

videoclip.close()
audioclip.close()
print("Video successfullly downloaded from", link)
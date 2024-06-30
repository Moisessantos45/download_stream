import flet as ft
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# path = os.path.dirname(__file__)

# url = "https://youtu.be/kOkQ4T5WO9E?si=aN_AgzvZKfa2FzTI"
# yt = YouTube(url)
# itag = 137
# itag2 = 140
# yt.streams.filter(only_audio=True)
# # streme = yt.streams.get_by_itag(itag=itag)
# streme2 = yt.streams.get_by_itag(itag=itag2)
# # streme.download()
# streme2.download()
# print("video: ", streme.default_filename)

# video_clip = VideoFileClip(streme.default_filename)
# audio_clip = AudioFileClip(streme2.default_filename)
# final_clip = video_clip.set_audio(audio_clip)
# final_clip.write_videofile("video_with_audio.mp4", encoder="libx264")


def main(page):
    url = ft.TextField(label="URL", autofocus=True)
    submit = ft.ElevatedButton("Download")

    def click(e):
        curret_url = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=curret_url)

    submit.on_click = click
    page.add(url, submit)


ft.app(target=main)

# para compilar el archivo de usa flet pack .\main.py --name descargar_videos --icon logo.png

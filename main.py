import flet as ft
from pytube import YouTube
import os


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

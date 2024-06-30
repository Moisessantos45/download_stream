import flet as ft
from tkinter import Tk, filedialog
from pytube import Playlist, YouTube
import os
from moviepy.editor import AudioFileClip


def download_cancion(url, format, save_path, progress_text, status_text, page: ft.Page):
    yt = YouTube(url)
    progress_text.value = f"Descargando: {yt.title}"
    status_text.value = "En progreso..."
    page.update()

    if format == "MP4":
        video = (
            yt.streams.filter(
                progressive=True, resolution="1080p", file_extension="mp4"
            ).first()
            or yt.streams.filter(
                progressive=True, resolution="720p", file_extension="mp4"
            ).first()
            or yt.streams.filter(
                progressive=True, file_extension="mp4"
            ).get_highest_resolution()
        )

        if video:
            video.download(output_path=save_path)
        else:
            print(f"No se encontró video disponible para: {yt.title}")

    elif format == "MP3":
        audio_stream = yt.streams.filter(only_audio=True, abr="128kbps").first()
        out_file = audio_stream.download(output_path=save_path)

        mp4_path = os.path.join(save_path, out_file)
        mp3_path = os.path.join(save_path, os.path.splitext(out_file)[0] + ".mp3")

        audio_clip = AudioFileClip(mp4_path)
        audio_clip.write_audiofile(mp3_path)
        os.remove(mp4_path)

    progress_text.value = "Descarga completada"
    status_text.value = "El video ha sido descargado."
    page.update()


def download_videos(url, format, save_path, progress_text, status_text, page: ft.Page):
    playlist = Playlist(url)

    total_videos = len(playlist.video_urls)
    for index, video_url in enumerate(playlist.video_urls):
        yt = YouTube(video_url)
        progress_text.value = f"Descargando {index + 1} de {total_videos}: {yt.title}"
        status_text.value = "En progreso..."
        page.update()

        if format == "MP4":
            video = (
                yt.streams.filter(
                    progressive=True, resolution="1080p", file_extension="mp4"
                ).first()
                or yt.streams.filter(
                    progressive=True, resolution="720p", file_extension="mp4"
                ).first()
                or yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).get_highest_resolution()
            )

            if video:
                video.download(output_path=save_path)
            else:
                print(f"No se encontró video disponible para: {yt.title}")

        elif format == "MP3":
            video = yt.streams.filter(only_audio=True, abr="128kbps").first()
            out_file = video.download(output_path=save_path)

            mp4_path = os.path.join(save_path, out_file)
            mp3_path = os.path.join(save_path, os.path.splitext(out_file)[0] + ".mp3")

            audio_clip = AudioFileClip(mp4_path)
            audio_clip.write_audiofile(mp3_path)
            os.remove(mp4_path)

    progress_text.value = "Descarga completada"
    status_text.value = "Todos los videos han sido descargados."
    page.update()


def main(page: ft.Page):
    def select_folder(e):
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        root.update()
        folder_selected = filedialog.askdirectory()
        save_path.value = folder_selected
        page.update()

    def start_download(e):
        if playlist_url.value and save_path.value and format_selector.value:
            if select_opcion.value == "Descargar canciones":
                download_cancion(
                    playlist_url.value,
                    format_selector.value,
                    save_path.value,
                    progress_text,
                    status_text,
                    page,
                )
            else:
                download_videos(
                    playlist_url.value,
                    format_selector.value,
                    save_path.value,
                    progress_text,
                    status_text,
                    page,
                )

    select_opcion = ft.Dropdown(
        label="Seleccione una opción",
        options=[
            ft.dropdown.Option("Descargar canciones"),
            ft.dropdown.Option("Descargar una lista de reproducción"),
        ],
    )

    playlist_url = ft.TextField(label="URL de la playlist")
    format_selector = ft.Dropdown(
        label="Formato",
        options=[
            ft.dropdown.Option("MP3"),
            ft.dropdown.Option("MP4"),
        ],
    )
    save_path = ft.TextField(label="Carpeta de destino", read_only=True)
    select_button = ft.ElevatedButton("Seleccionar carpeta", on_click=select_folder)
    download_button = ft.ElevatedButton("Descargar", on_click=start_download)
    progress_text = ft.Text(value="Progreso de la descarga")
    status_text = ft.Text(value="Estado")

    page.add(
        select_opcion,
        playlist_url,
        format_selector,
        save_path,
        select_button,
        download_button,
        progress_text,
        status_text,
    )


ft.app(target=main)

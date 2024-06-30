from pytube import Playlist, YouTube

# URL de la playlist de YouTube
playlist_url = "https://www.youtube.com/watch?v=F4JD-UxE38E&list=PL4Tdvgcfby6IHlUzDCANVBZfa-SnvmUWl"
playlist = Playlist(playlist_url)

# Directorio donde se guardarán los archivos MP4
save_path = "./"  # Cambia esto por la ruta donde deseas guardar los archivos

for video_url in playlist.video_urls:
    yt = YouTube(video_url)
    # Intenta descargar en 1080p progresivo
    video = yt.streams.filter(
        progressive=True, resolution="1080p", file_extension="mp4"
    ).first()
    if not video:
        # Si no hay 1080p, intenta con 720p progresivo
        video = yt.streams.filter(
            progressive=True, resolution="720p", file_extension="mp4"
        ).first()
    if not video:
        # Si no hay 720p, descarga el mejor stream progresivo disponible
        video = yt.streams.filter(
            progressive=True, file_extension="mp4"
        ).get_highest_resolution()

    if video:
        video.download(output_path=save_path)
        print(f"Descargado: {video.title} en resolución {video.resolution}")
    else:
        print(f"No se encontró video disponible para: {yt.title}")

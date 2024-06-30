from pytube import Playlist, YouTube

# URL de la playlist de YouTube
playlist_url = "https://www.youtube.com/watch?v=F4JD-UxE38E&list=PL4Tdvgcfby6IHlUzDCANVBZfa-SnvmUWl"
playlist = Playlist(playlist_url)

for video_url in playlist.video_urls:
    yt = YouTube(video_url)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")

    if streams:
        print(f"Resoluciones disponibles para {yt.title}:")
        for stream in streams:
            print(f"- {stream.resolution}")
    else:
        print(f"No se encontró video disponible para: {yt.title}")

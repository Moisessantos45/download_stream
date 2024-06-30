from pytube import Playlist, YouTube
import os
from moviepy.editor import AudioFileClip

# URL de la playlist de YouTube
playlist_url = "https://www.youtube.com/watch?v=KVHmtJDnj_0&list=PL4Tdvgcfby6ISCof4fRp6qbUvFIV-Jydo"
playlist = Playlist(playlist_url)

# Directorio donde se guardarán los archivos MP3
save_path = "./"  # Cambia esto por la ruta donde deseas guardar los archivos

for video_url in playlist.video_urls:
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=save_path)

    # Carga el archivo descargado, que está en formato MP4
    mp4_path = os.path.join(save_path, out_file)
    mp3_path = os.path.join(save_path, os.path.splitext(out_file)[0] + ".mp3")

    # Convierte de MP4 a MP3
    audio_clip = AudioFileClip(mp4_path)
    audio_clip.write_audiofile(mp3_path)

    # Opcional: elimina el archivo MP4 original
    os.remove(mp4_path)
    print(f"Descargado y convertido a MP3: {mp3_path}")

from pytube import YouTube
import os

def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def check_youtube_url(url):
    try:
        YouTube(url)
        return True
    except:
        return False

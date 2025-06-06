import subprocess
from yt_dlp import YoutubeDL
import os

def get_video_title(url):
    ydl_opts = {'quiet': True, 'skip_download': True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['title']

def download_video(url, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_filename,
        'merge_output_format': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        '-ar', '44100',
        '-y',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted to MP3:", output_file)
    except subprocess.CalledProcessError:
        print("FFmpeg conversion failed.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")

    print("Getting video title...")
    title = get_video_title(video_url)
    safe_title = "".join(c for c in title if c.isalnum() or c in " ._-").strip()  # sanitize filename

    video_file = f"{safe_title}.mp4"
    audio_file = f"{safe_title}.mp3"

    print("Downloading video...")
    download_video(video_url, video_file)

    print("🎧 Converting to MP3...")
    convert_video_to_mp3(video_file, audio_file)

    if os.path.exists(video_file):
        os.remove(video_file)
        print("Removed temporary video file.")

    print("Done! MP3 saved as:", audio_file)

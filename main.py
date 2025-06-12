import streamlit as st
from audio_downloader import get_video_title, download_video as download_audio_video, convert_video_to_mp3
from video_downloader import download_video as download_full_video
import os

st.title("YouTube Video/Audio Downloader")

url = st.text_input("Enter YouTube video URL")

if url:
    title = get_video_title(url)
    safe_title = "".join(c for c in title if c.isalnum() or c in " ._-").strip()
    video_file = f"{safe_title}.mp4"
    audio_file = f"{safe_title}.mp3"

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Download Audio (MP3)"):
            with st.spinner("Downloading audio..."):
                download_audio_video(url, video_file)
                convert_video_to_mp3(video_file, audio_file)
                if os.path.exists(video_file):
                    os.remove(video_file)
                st.success(f"✅ MP3 saved as: {audio_file}")

    with col2:
        if st.button("Download Full Video (MP4)"):
            with st.spinner("Downloading video..."):
                download_full_video(url)
                st.success("✅ Video downloaded successfully!")


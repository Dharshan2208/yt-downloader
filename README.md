# YouTube Downloader

A simple Python tool to download YouTube videos or just the audio (as MP3). I made this because I was bored of online converters...

---

## Files

- `video_downloader.py` → Downloads full YouTube videos (best quality)
- `audio_downloader.py` → Downloads and converts videos to MP3
- `main.py` → A Streamlit app for easy UI

---

## Required

- Python 3.6 or higher
- FFmpeg (for audio conversion)
  - Windows: [Download FFmpeg](https://ffmpeg.org/download.html)
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`
- Python packages:
  ```bash
  pip install yt-dlp streamlit
  ```

---

## 🚀 How to Use

### Run from Terminal

**To download a video:**
```bash
python video_downloader.py
```

**To download MP3:**
```bash
python audio_downloader.py
```

**Or launch the UI:**
```bash
streamlit run main.py
```

---

## Features

- High-quality MP3 conversion (192 kbps, 44.1 kHz)
- Download videos in top quality
- Best quality video/audio download
- Clean file names
- Deletes temp files after conversion

---

## Disclaimer

- This is for personal use only.
- Don’t use it to download copyrighted stuff!
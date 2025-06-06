# YouTube Downloader

Python scripts I made for downloading YouTube videos and converting audio to MP4 & MP3 using ffmpeg. Built this for my own needs but you can also use
and also because I got bored of online converters!

## 📁 Files Overview

- **`video_downloader.py`** - Downloads YouTube videos in the best available quality
- **`audio_downloader.py`** - Downloads YouTube videos and automatically converts them to MP3

## 🛠️ Prerequisites

### Required Software

- **Python 3.6+**
- **FFmpeg** - Required for audio conversion
  - Windows: Download from [ffmpeg.org]
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

### Required Python Packages

```bash
pip install yt-dlp
```

Note: `subprocess` and `os` are built-in Python modules.

## 🚀 Usage

### 1. Download YouTube Videos (`video_downloader.py`)

Downloads videos in the best available quality (video + audio combined).

```bash
python video_downloader.py
```

- Enter the YouTube URL when prompted
- Video saves as `[Video Title].mp4`

### 2. Download YouTube Audio as MP3 (`audio_downloader.py`)

Downloads YouTube videos and automatically converts them to MP3 format.

```bash
python audio_downloader.py
```

- Enter the YouTube URL when prompted
- Audio saves as `[Video Title].mp3`
- Temporary video file is automatically deleted

## ⚙️ Audio Quality Settings

All MP3 conversions use the following high-quality settings:

- **Codec**: LAME MP3 encoder
- **Bitrate**: 192 kbps
- **Sample Rate**: 44.1 kHz

## 📋 Features

- High-quality MP3 conversion (192 kbps, 44.1 kHz)
- Automatic filename sanitization
- Temporary file cleanup
- Best quality video/audio download

## ⚠️Notice

- If you can't hear any sound when playing the video, try using VLC Media Player instead - it works with many different audio types than most other video players.

## ⚠️ DISCLAIMER

- Downloading copyrighted material without proper authorization is illegal and strictly prohibited.

- I don't take any responsibility for how this tool is used.
  By using this tool, you agree that you are solely responsible for your actions and compliance with applicable laws.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve these tools!

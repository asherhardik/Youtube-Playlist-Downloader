import yt_dlp

# Ask the user for the YouTube playlist link
playlist_link = input("Enter the YouTube playlist link: ")

# Set options for the highest quality video and audio
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # This selects the best video + audio combination
    'outtmpl': '%(title)s.%(ext)s',  # Use the video title as the filename (with extension)
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',  # Convert the video to the desired format, if needed
        'preferedformat': 'mp4',  # Preferred format after conversion (you can change this)
    }],
    'ffmpeg_location': r'C:\ffmpeg\bin',  # Path to ffmpeg if not in PATH
    'noplaylist': False,  # Ensure playlist downloading is enabled
    'extractaudio': False,  # Disable audio-only download
}

# Download the playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_link])

from pytubefix import YouTube

def download_youtube_video(url):
    vid = YouTube(url)

    video_download = vid.streams.get_highest_resolution()
    audio_download = vid.streams.get_audio_only()

    entry = vid.title

    print(f"\nVideo found: {entry}\n")

    print(f"Downloading Video...")
    video_download.download(filename=f"{entry}.mp4")

    print("Downloading Audio...")
    audio_download.download(filename=f"{entry}.mp3")

    print("Download Completed")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_youtube_video(url)
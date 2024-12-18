import os
from django.utils.text import slugify
from django.http import JsonResponse
from django.conf import settings
from pytubefix import YouTube

def get_unique_slug(slug, extension):
    """
    Ensure the slug is unique by appending a suffix if needed.
    """
    unique_slug = slug
    counter = 1
    while os.path.exists(os.path.join(settings.MEDIA_ROOT, f"{unique_slug}.{extension}")):
        unique_slug = f"{slug}-{counter}"
        counter += 1
    return unique_slug

def youtube_download_service(youtube_url):
    # Download the YouTube video as audio
    yt = YouTube(youtube_url)

    # Create a slug from the video title
    video_title_slug = slugify(yt.title)
    
    # Ensure the slug is unique in the MEDIA_ROOT directory
    unique_slug = get_unique_slug(video_title_slug, 'mp3')
    path = settings.MEDIA_ROOT + '/temp/'
    yt.streams.filter(only_audio=True).first().download(output_path=path, filename=f"{unique_slug}.mp3")

    return unique_slug

from django.http import JsonResponse
from django.conf import settings
from myapp.services.youtube_download import youtube_download_service


def index(request):
    return JsonResponse({
        'creator': 'Suman Thapa'
    })

def download_youtube_audio(request):
    youtube_url = request.GET.get('url', None)
    if not youtube_url:
        return JsonResponse({'error': 'No YouTube URL provided.'}, status=400)

    try:
        unique_slug = youtube_download_service(youtube_url)
        download_link = request.build_absolute_uri(f"/media/temp/{unique_slug}.mp3")
        return JsonResponse({'download_link': download_link}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

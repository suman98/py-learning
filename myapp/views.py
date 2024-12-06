from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from myapp.services.youtube_download import youtube_download_service
from .models import UserIP

def get_client_ip(request):
    """
    Retrieves the client's IP address from the Django request object.

    Args:
        request (HttpRequest): The Django request object.

    Returns:
        str: The client's IP address.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If there are multiple IPs, take the first one
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        # Fallback to REMOTE_ADDR if no X-Forwarded-For is present
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    return JsonResponse({
        'creator': 'Railway Gmail'
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


def capture_ip(request):
    user_ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Save IP and User-Agent
    UserIP.objects.create(ip_address=user_ip)

    return render(request, 'full_image.html')
 

def show_captured_ip(request):
    # Check if the required query parameter is present
    if request.GET.get('sps') != 'rfgx':
        return JsonResponse({"error": "Unauthorized access"}, status=403)
    user_ips = UserIP.objects.all().order_by('-created_at')

    # Create a list of dictionaries to represent the data
    data = [
        {
            "id": ip.id,
            "ip_address": ip.ip_address,
            "captured_at": ip.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for ip in user_ips
    ]

    # Return the data as JSON
    return JsonResponse({"captured_ips": data}, safe=False)
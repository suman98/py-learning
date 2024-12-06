"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('download/', views.download_youtube_audio, name='get_youtube_download_link'),
    path('get-check/', views.capture_ip, name='get_ip'),
    path('0-02-03-b562a2209993e778a03313ebeeca865949ae9564c37fe3bf9117c45c7ad0c563_21b68c0b2e7/', views.capture_ip, name='capture_ip'),
    path('show-check/', views.show_captured_ip, name='show_captured_ip'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

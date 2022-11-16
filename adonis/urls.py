
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from adonis import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exe.urls'))
# Это ссылка для MEDIA-файлов
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
from django.urls import path

from bc import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

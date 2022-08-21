from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('opinion/', opinion, name="opinion")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
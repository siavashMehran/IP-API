
from API_main.views import home
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from API_main import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', home, name='indexpage')


]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

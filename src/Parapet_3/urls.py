
from django.contrib import admin
from django.urls import include,path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'), name='accounts'),
    path('social/', include('social.urls'), name='social'),
    path('static_pages/', include('static_pages.urls'), name='static'),
    path('chat/', include('chat.urls'), name='chat'),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

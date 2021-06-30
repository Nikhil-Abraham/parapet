
from django.contrib import admin
from django.urls import include,path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'), name='accounts'),
    path('social/', include('social.urls'), name='social'),
    path('chat/', include('chat.urls'), name='chat'),
    path('chat2/', include('chat2.urls'), name='chat2'),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path,include
from . import views

app_name = 'static'

urlpatterns = [
  path('newsletter/',views.newsletter,name='newsletter'),
  path('topStories/',views.topStories,name='topStories'), 
]
from django.urls import path
from . import views

app_name = 'chat2'

urlpatterns = [
  path('', views.home, name="home"),
]
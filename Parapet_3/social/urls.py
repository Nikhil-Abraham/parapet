from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.index,name='index'),
  path('f_logout',views.feed_logout,name='feed_logout'),
  path('profiles/<str:pk>', views.profile,name="profile")
]
from django.urls import path,include
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.index,name='index'),
  path('explore',views.explore,name='explore'),
  path('user_profile',views.user_profile,name='user_profile'),
  # path('profiles/<str:pk>', views.profile,name="profile")
]
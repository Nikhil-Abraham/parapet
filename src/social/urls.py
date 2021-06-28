from django.urls import path,include
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.index,name='index'),
  path('explore/',views.explore,name='explore'),
  path('settings/',views.settings,name='settings'),
  path('user_profile/',views.user_profile,name='user_profile'),
  # path('profiles/<str:pk>', views.profile,name="profile")

  path('explore/article/<str:pk>/',views.article,name='article'),

  path('post/',views.post_article,name='post_article'),
]
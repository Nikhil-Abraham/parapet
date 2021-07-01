from django.urls import path,include
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.socialHome,name='index'),
  path('explore/',views.explore,name='explore'),
  path('settings/',views.settings,name='settings'),
  path('user_profile/<str:pk>',views.user_profile,name='user_profile'),

  path('newsletter/',views.newsletter,name='newsletter'),
  path('topStories/',views.topStories,name='topStories'), 

  path('explore/article/<str:pk>/',views.article,name='article'),

  path('post/',views.post_article,name='post_article'),
  path('post/<str:pk>',views.postDetail,name='postDetail'),
  path('post/edit/<str:pk>',views.PostEditView.as_view(),name='postEdit'),
  path('post/delete/<str:pk>',views.PostDeleteView.as_view(),name='postDelete'),
  path('hv7/',views.hv7),
]
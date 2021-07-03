from django.urls import path,include
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.socialHome,name='index'),
  path('explore/',views.explore,name='explore'),
  path('settings/',views.settings,name='settings'),

  path('newsletter/',views.newsletter,name='newsletter'),
  path('topStories/',views.topStories,name='topStories'), 

  path('explore/article/<str:pk>/',views.article,name='article'),

  path('post/',views.post_article,name='post_article'),
  path('post/<str:pk>',views.postDetail,name='postDetail'),
  path('post/edit/<str:pk>',views.PostEditView.as_view(),name='postEdit'),
  path('post/delete/<str:pk>',views.PostDeleteView.as_view(),name='postDelete'),
  path('post/<int:pk>/like',views.addLike, name='like'),
  path('post/<int:pk>/dislike',views.dislike, name='dislike'),


  path('user_profile/<str:pk>',views.user_profile,name='user_profile'),
  path('user_profile/<str:pk>/follower/add',views.addFollower,name='addFollower'),
  path('user_profile/<str:pk>/follower/remove',views.removeFollower,name='removeFollower'),

  path('inbox/', views.listThreads, name='inbox'),
  path('inbox/createThread/', views.createThread, name='create-thread'),
  path('inbox/<int:pk>/', views.threadView, name='thread'),
  path('inbox/<int:pk>/create-message/',views.CreateMessage.as_view(), name='create-message')

]
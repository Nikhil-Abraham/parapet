from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
  path('',views.index,name='index'),
  path('logout_f',views.logout_f,name='logout_f'),
  path('profiles/<str:pk>', views.profile,name="profile")
]
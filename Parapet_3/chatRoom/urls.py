from django.urls import path,include
from . import views

app_name = 'chatRoom'

urlpatterns = [
  path('<str:room_name>', views.chatIndex, name='chatIndex'),

]
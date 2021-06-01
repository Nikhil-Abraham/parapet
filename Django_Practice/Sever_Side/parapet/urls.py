from django.urls import path
from . import views

urlpatterns = [
  path("",views.index, name="index"),
  path("neha",views.neha, name="neha"),
  path("login",views.login, name="login")
]
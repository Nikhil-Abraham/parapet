from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):

      
      return view_func(request, *args, **kwargs)
    return wrapper_func
  return decorator

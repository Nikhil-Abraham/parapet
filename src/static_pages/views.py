from django.shortcuts import render, redirect
from accounts.models import Parapet_User
from django.contrib.auth.models import User

# Create your views here.
def newsletter(request):
  return render(request, 'static_pages/newsletter.html')

def topStories(request):
  return render(request, 'static_pages/top-stories.html')


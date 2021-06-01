from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello World!")

def neha(request):
  return HttpResponse("Hello, Neha!")

def login(request):
  return render("login.html")
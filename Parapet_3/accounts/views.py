from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "index.html")

def signup(request):
  pass

def login(request):
  pass

def logout(request):
  pass

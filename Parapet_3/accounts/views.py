from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, "index.html")

def register(request):
  if request.method == "POST":
    first_name = request.POST["first_name"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    username = email

    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, "User Exists")
        return redirect('register')
      else: 
        user = User.objects.create_user(username=username,email=email, first_name=first_name,password=password1)
        user.save()
        user = auth.authenticate(username=username,password=password1)
        auth.login(request, user)
        
    else:
      messages.info(request, "Passwords Dont Match")
      return redirect('register')
    return redirect('index')

  else:
    return render(request, "SignUp.html")


def login(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('index')
    else:
      messages.info(request, "Invalid Credentials")
      return redirect('login')


  else:
    return render(request, "login.html")

def logout(request):
  auth.logout(request)
  return redirect('index')

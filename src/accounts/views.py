from accounts.models import Parapet_User
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user


# Create your views here.
def home(request):
  return render(request, "index.html")

@unauthenticated_user
def register(request):
  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    username = email

    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, "User Exists")
        return redirect('accounts:register')
      else: 
        user = User.objects.create_user(username=username,email=email, first_name=first_name, last_name=last_name, password=password1)
        user.save()
        Parapet_User.objects.create(
          user=user,
          name=user.first_name+" "+user.last_name,
          email=user.email,
          username=user.email
        )
        return redirect('accounts:login')  
    else:
      messages.info(request, "Passwords Dont Match")
      return redirect('accounts:register')

  else:
    return render(request, "SignUp.html")

@unauthenticated_user
def login(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('social:index')
    else:
      messages.info(request, "Invalid Credentials")
      return redirect('accounts:login')


  else:
    return render(request, "login.html")

def logout(request):
  auth.logout(request)
  return redirect('accounts:home')

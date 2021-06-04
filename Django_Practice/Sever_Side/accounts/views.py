from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from . import views

# Create your views here.
def register(request):
  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    username = request.POST["username"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]

    if password1 == password2:
      if User.objects.filter(username=username).exits():
        print("Username Taken")
      elif User.objects.filter(email=email).exists():
        print("Email Taken")
      else:
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
      print("User Created")
      
    else:
      print("password dosent match")

    return redirect('/')

  else:
    return render(request,"register.html")

def login(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request)
      return redirect('/')
    else:
      message = "Invalid Credentials"
      return redirect("login", {
        "message": message
      })


  else:
    return render(request, "login.html")


def logout(request):
  auth.logout(request)
  return redirect('/')
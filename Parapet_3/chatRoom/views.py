from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from django.urls import reverse

from django.contrib.auth.decorators import login_required


from accounts.models import Parapet_User
from django.contrib.auth.models import User


def chatIndex(request,room_name):
  pass

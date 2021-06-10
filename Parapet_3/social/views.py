from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Post,PostArticle
from accounts.models import Parapet_User
from .forms import PostArticleForm,PostFeedForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
  if request.method == "POST":
    posts = Post.objects.all().order_by('-created_on')
    form = PostFeedForm(request.POST)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.author = Parapet_User.objects.get(user = request.user)
      new_post.save()

    return HttpResponseRedirect(request.path)

  else:
    posts = Post.objects.all().order_by('-created_on')
    form = PostFeedForm()

    user = request.user
    current_user = Parapet_User.objects.get(user = user)

    context = {
      "post_list": posts,
      'form' : form,
      'user': current_user
    }
    return render(request, 'social/mbrpage.html', context)

@login_required(login_url='accounts:login')
def explore(request):

  articles = PostArticle.objects.all().order_by('-created_on')

  context = {
    'article_list': articles
  }

  return render(request, 'social/explore.html', context)

@login_required(login_url='accounts:login')
def user_profile(request):
  user = request.user
  current_user = Parapet_User.objects.get(user = user)

  posts = Post.objects.all().filter(author=current_user)

  context = {
    'user': current_user,
    'post_list':posts,
  }
  return render(request, 'social/user_profile.html', context)
from django.shortcuts import redirect, render
from .models import Post,PostArticle
from .forms import PostArticleForm,PostFeedForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  if request.method == "POST":
    posts = Post.objects.all().order_by('-created_on')
    form = PostFeedForm(request.POST)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.author = request.user
      new_post.save()

      context = {
    "post_list": posts,
    'form' : form,
    }
    return render(request, 'social/mbrpage.html', context)

  else:
    posts = Post.objects.all().order_by('-created_on')
    form = PostFeedForm()

    user = request.user
    current_user = User.objects.get(username = user)

    context = {
      "post_list": posts,
      'form' : form,
      'first_name' : current_user.first_name,
      'last_name' : current_user.last_name,
    }
    return render(request, 'social/mbrpage.html', context)

def logout_f(request):
  return redirect('accounts:logout')
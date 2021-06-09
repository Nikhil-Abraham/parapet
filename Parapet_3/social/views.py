from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  if request.method == "POST":
    posts = Post.objects.all().order_by('-created_on')
    form = PostForm(request.POST)
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
    form = PostForm()

    context = {
      "post_list": posts,
      'form' : form,
    }
    return render(request, 'social/mbrpage.html', context)
  
def profile(request, pk):
  user = User.objects.get(id=pk)
  posts = user.post_set.all().order_by('-created_on')

  context = {
    'post_list' : posts, 
    'user' : user
  }

  return render(request, 'social/profile.html', context)

def logout_f(request):
  return redirect('accounts:logout')
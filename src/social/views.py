from django.db.models import query
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from .models import Comment, Post,PostArticle
from accounts.models import Parapet_User
from .forms import PostArticleForm, PostFeedForm, UserForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='accounts:login')
def socialHome(request):
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
def postDetail(request, pk):
  if request.method == "POST":
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.author = Parapet_User.objects.get(user = request.user)
      new_comment.post = post
      new_comment.save()
    
    comments = Comment.objects.filter(post=post).order_by('-created_on')


    context = {
      'post':post,
      'form':form,
      'comments':comments,
    }
    return render(request, 'social/post_detail.html', context)

  else:
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by('-created_on')

    context = {
      'post':post,
      'form':form,
      'comments':comments,
    }
    return render(request, 'social/post_detail.html', context)

class PostEditView(UpdateView):
  model = Post
  fields = ['body']
  template_name = 'social/post_edit.html'

  def get_success_url(self):
      pk = self.kwargs['pk']
      return reverse_lazy('social:postDetail', kwargs={'pk':pk})


class PostDeleteView(DeleteView):
  model = Post
  template_name = 'social/post_delete.html'

  success_url = reverse_lazy('social:index')


@login_required(login_url='accounts:login')
def explore(request):
  articles = PostArticle.objects.all().order_by('-created_on')

  context = {
    'article_list': articles
  }

  return render(request, 'social/explore.html', context)



@login_required(login_url='accounts:login')
def user_profile(request, pk):

  profile = Parapet_User.objects.get(pk=pk)
  user = profile.user
  posts = Post.objects.filter(author=profile).order_by('-created_on')

  followers = profile.followers.all()

  if len(followers) == 0:
      is_following = False

  for follower in followers:
      if follower == request.user:
          is_following = True
          break
      else:
          is_following = False

  number_of_followers = len(followers)

  context = {
      'user': user,
      'profile': profile,
      'post_list': posts,
      'number_of_followers': number_of_followers,
      'is_following': is_following,
  }
  return render(request, 'social/user_profile.html', context)


@login_required(login_url='accounts:login')
def settings(request):
  user = request.user
  p_user = user.parapet_user
  current_user = Parapet_User.objects.get(user = user)

  posts = Post.objects.all().filter(author=current_user)

  form = UserForm(instance=p_user)

  if request.method == 'POST':
    form = UserForm(request.POST, request.FILES,instance=p_user)
    if form.is_valid():
      form.save()

  context = {
    'user':current_user,
    'post_list':posts,
    'form':form,
  }
  return render(request, 'social/settings.html', context)


@login_required(login_url='accounts:login')
def article(request,pk):
    article = PostArticle.objects.all().get(id=pk)
    # post = PostArticle.objects.all()

    context = {
      'article_item':article,
    }
    return render(request, 'social/article_item.html', context)


@login_required(login_url='accounts:login')
def post_article(request):
    if request.method=='POST':
      a_user=Parapet_User.objects.get(user = request.user)
      a_form = PostArticleForm(request.POST, request.FILES)
      if a_form.is_valid():
        new_post = a_form.save(commit=False)
        new_post.author = a_user
        new_post.save()
        
        #a_form.save()
        print("Article is Valid")
        return redirect('../explore/')
      print("Invalid Article")

    else:
      form = PostArticleForm()
      user = request.user
      current_user = Parapet_User.objects.get(user = user)

    context = {
      'form' : form,
      'user': current_user
    }
    return render(request,'social/post_article.html',context)

def newsletter(request):
  return render(request, 'social/newsletter.html')

def topStories(request):
  return render(request, 'social/top-stories.html')


def hv7(request):
  return render(request, 'social/hv7.html')


def addFollower(request,pk):
  profile = Parapet_User.objects.get(pk = pk)
  profile.followers.add(request.user)
  
  return redirect('social:user_profile', pk=profile.pk)

def removeFollower(request,pk):
  profile = Parapet_User.objects.get(pk = pk)
  profile.followers.remove(request.user)

  return redirect('social:user_profile', pk=profile.pk)

def addLike(request, pk):
  post = Post.objects.get(pk=pk)

  is_dislike = False

  for dislike in post.dislikes.all():
    if dislike == request.user:
      is_dislike = True
      break
  
  if is_dislike:
    post.dislikes.remove(request.user)
  
  is_like = False

  for like in post.likes.all():
    if like == request.user:
      is_like = True
      break

  if not is_like:
    post.likes.add(request.user)
  if is_like:
    post.likes.remove(request.user)

  next = request.POST.get('next','/')
  return HttpResponseRedirect(next)



  
def dislike(request, pk):
  post = Post.objects.get(pk=pk)

  is_like = False

  for like in post.likes.all():
    if like == request.user:
      is_like = True
      break

  if is_like:
    post.likes.remove(request.user)

  is_dislike = False

  for dislike in post.dislikes.all():
    if dislike == request.user:
      is_dislike = True
      break
  
  if not is_dislike:
    post.dislikes.add(request.user)
  if is_dislike:
    post.dislikes.remove(request.user)


  next = request.POST.get('next','/')
  return HttpResponseRedirect(next)



class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = Parapet_User.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }

        return render(request, 'social/search.html', context)

   

    

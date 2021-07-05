from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.models import Parapet_User



class Post(models.Model):
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(Parapet_User, on_delete=models.CASCADE)
  likes = ManyToManyField(User, blank=True, related_name='likes')
  dislikes = ManyToManyField(User, blank=True, related_name='dislikes')


class PostArticle(models.Model):
  title = models.TextField(default='Title Goes Here ... ')
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(Parapet_User, on_delete=models.CASCADE)
  article_pic = models.ImageField(upload_to = 'ArticlePictures',null=True,blank=True)

  def __str__(self):
    return f"{self.title} : {self.body}"


class Comment(models.Model):
  comment = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author =  models.ForeignKey(Parapet_User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)


class ThreadModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
  thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
  sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  body = models.CharField(max_length=1000)
  date = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False) 
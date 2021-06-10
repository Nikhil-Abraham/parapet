from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.models import Parapet_User


# class Parapet_User(models.Model):
#   user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#   name = CharField(max_length=60, null=True)
#   phone = CharField(max_length=60, null=True)
#   email = CharField(max_length=60, null=True)
#   date_created = models.DateTimeField(auto_now_add=True, null=True)

#   def __str__(self):
#     return self.name
  

class Post(models.Model):
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(Parapet_User, on_delete=models.CASCADE)


class PostArticle(models.Model):
  title = models.TextField(default='Title Goes Here ... ')
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(Parapet_User, on_delete=models.CASCADE)
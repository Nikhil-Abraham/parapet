from django.db import models


# Create your models here.
class Users(models.Model):
  username = models.CharField(max_length=30)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.id}: username: {self.username}  email: {self.email}  password: {self.password}"
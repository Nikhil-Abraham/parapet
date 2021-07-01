from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings


class PublicChatRoom(models.Model):
  title = models.CharField(max_length=255, unique=True, blank=False)
  user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="users who are connected to chat")

  def __str__(self):
      return self.title

  def connect_user(self, user):
    #return True if user is added to the user list
    is_user_added = False
    if not user in self.users.all():
      self.users.add(user)
      self.save()
      is_user_added  = True
    elif user in self.users.all():
      is_user_added = True
    return is_user_added
  
  def disconnect_user(self, user):
    #return True if user is removed from the users list
    is_user_removed = False
    if not user in self.users.all():
      self.users.remove(user)
      self.save()
      is_user_removed  = True
    return is_user_removed

  @property
  def group_name(self):
    #returns the chanels group name that sockets should subscribe to and get sent messages

    return f"PublicChatRoom-{self.id}"



class PublicRoomChatManager(models.Manager):
  def by_room(self, room):
    qs = PublicRoomChatMessage.objects.filter(room=room).order_by("-timestamp")
    return qs



class PublicRoomChatMessage(models.Model):
  #chat message created by a user inside a public chat room

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)
  content = models.TextField(unique=False, blank=False)

  obejcts = PublicRoomChatManager()

  def __str__(self):
    return self.content

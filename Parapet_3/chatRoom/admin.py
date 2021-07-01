from django.contrib import admin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import models

from chatRoom.models import PublicChatRoom, PublicRoomChatMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
  list_display = ['id', 'title']
  search_fields = ['id', 'title']
  list_display = ['id']

  class Meta:
    mdoel = PublicChatRoom

admin.site.register(PublicChatRoom, PublicChatRoomAdmin)

class CachingPaginator(Paginator):
  def _get_count(self):
    if not hasattr(self, "_count"):
      self._count = None
    if self._count is None:
      try:
        key = "adm:{0}:count".format(hash(self.object_list.querry.__str__()))
        self._count = cache.get(key, -1)
        if self._count == -1:
          self._count = super().count
          cache.set(key, self._count, 3600)
      except:
        self._count = len(self.object_list)
    return self._count
  count = property(_get_count)


class PublicRoomChatMessageAdmin(admin.ModelAdmin):
  list_filter = ['room', 'user', 'timestamp']
  list_display = ['room', 'user', 'timestamp', 'content']
  search_fields = ['room__title', 'user__username', 'timestamp', 'content']
  readonly_fields = ['id','room', 'user', 'timestamp']

  show_full_result_count = False
  paginator = CachingPaginator

  class Meta:
    model = PublicRoomChatMessage


admin.site.register(PublicRoomChatMessage, PublicRoomChatMessageAdmin)
from django.contrib import admin
from .models import Post, PostArticle, MessageModel, ThreadModel



admin.site.register(Post)
admin.site.register(PostArticle)
admin.site.register(ThreadModel)
admin.site.register(MessageModel)
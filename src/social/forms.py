from django import forms
from django.forms.widgets import Widget
from .models import Post, PostArticle, Comment
from accounts.models import Parapet_User

class PostFeedForm(forms.ModelForm):
  
  body = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
      'placeholder' : 'Say Something...',
      'class' : 'text_area_field',
    })
  )


  class Meta:
    model = Post
    fields = ['body']


class PostArticleForm(forms.ModelForm):
  title = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
     'placeholder' :'Add Title ...',
     'class' : 'title_field',
    })
  )
  
  body = forms.CharField(
    label='',
    widget=forms.Textarea(attrs={
      'rows' : '3',
      'placeholder' : 'Say Something...',
      'class' : 'text_area_field',
    })
  )
  class Meta:
    model = PostArticle
    fields = ['title','body','article_pic']

class UserForm(forms.ModelForm):
  class Meta:
    model = Parapet_User
    fields = '__all__'
    exclude = ['user']


class CommentForm(forms.ModelForm):
  comment = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
     'placeholder' :'Add Comment ...',
     'class' : 'text_area_field',
    })
  )


  class Meta:
    model = Comment
    fields = ['comment']
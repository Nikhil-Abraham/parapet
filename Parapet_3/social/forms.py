from django import forms
from django.forms.widgets import Widget
from .models import Post

class PostForm(forms.ModelForm):
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
    model = Post
    fields = ['title','body']
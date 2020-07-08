from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, ModelChoiceField

from blog.models import Post
from taggit.forms import TagWidget, TagField


class PostForm(ModelForm):
    tags = TagField(required=False, widget=TagWidget(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'tags')
        users = ModelChoiceField(queryset=User.objects.all())
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': TextInput(attrs={'type': 'hidden'}),
        }

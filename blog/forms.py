from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, ModelChoiceField

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')
        users = ModelChoiceField(queryset=User.objects.all())
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': TextInput(attrs={'type': 'hidden'})
        }

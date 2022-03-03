from socket import fromshare
from django import forms
from models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tage', 'author', 'body')

        widget = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
        }
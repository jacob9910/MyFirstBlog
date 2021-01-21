from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'title_image', 'author', 'content', 'category')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your own title for your post!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your own title for your post!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
        }
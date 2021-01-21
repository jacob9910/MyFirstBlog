from django.shortcuts import render
from blog.models import Category, Post
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm, EditForm


# Create your views here.
def index(req):
    context = {
    }

    return render(req, "index.html", context=context)

class HomeView(ListView):
    model = Post
    template_name = 'New.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'CreatePost.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'content']
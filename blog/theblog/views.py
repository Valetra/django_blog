from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
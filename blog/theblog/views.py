from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_details.html'
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import PostForm, EditForm

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
        
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        
        post_obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_obj.total_likes()

        liked = False
        if post_obj.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        context['total_likes'] = total_likes
        context['liked'] = liked

        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
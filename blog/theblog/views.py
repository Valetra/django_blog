from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, 
    DeleteView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post, Category
from .forms import PostForm, EditForm

#TODO: include in the executable function in the future to remove unused categories. 
def clear_category_list():
    cat_posts = Post.objects.all()
    cat_menu = Category.objects.all()

    post_categories_list = []

    for posts_item in cat_posts:
        post_categories_list.append(posts_item.category) 
    
    for menu_item in cat_menu:
        if str(menu_item) not in post_categories_list:
            q = Category.objects.get(name=menu_item)
            q.delete()

def get_category_menu_context(self, view, *args, **kwargs):
        category_menu = Category.objects.all()

        context = super(view, self).get_context_data(*args, **kwargs)
        context['category_menu']= category_menu
        return context

def CategoryView(request, category):
    category_menu = Category.objects.all()

    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category_menu': category_menu, 'category':category.title().replace('-', ' '), 'category_posts': category_posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, HomeView, *args, **kwargs)
        
class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, ArticleDetailView, *args, **kwargs)

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, AddPostView, *args, **kwargs)

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, AddCategoryView, *args, **kwargs)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UpdatePostView, *args, **kwargs)

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, DeletePostView, *args, **kwargs)
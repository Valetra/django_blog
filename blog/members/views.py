from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from theblog.views import get_category_menu_context

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('my_login')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserRegisterView, *args, **kwargs)

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/my_login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserLoginView, *args, **kwargs)
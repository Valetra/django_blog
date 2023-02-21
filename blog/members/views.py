from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


from theblog.views import get_category_menu_context

from members.forms import SignUpForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('my_login')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserRegisterView, *args, **kwargs)

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserEditView, *args, **kwargs)
  

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/my_login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserLoginView, *args, **kwargs)
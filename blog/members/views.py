from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm#, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from theblog.views import get_category_menu_context

from members.forms import SignUpForm, EditProfileForm, PasswordChangingForm

def password_success(request):
    return render(request, 'registration/password_success.html', {})    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('my_login')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserRegisterView, *args, **kwargs)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
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
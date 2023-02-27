from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from theblog.views import get_category_menu_context
from theblog.models import Profile

from members.forms import (
    SignUpForm,
    EditUserSettingsForm,
    PasswordChangingForm, 
    ProfilePageForm,
)
class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, CreateProfilePageView, *args, **kwargs)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, EditProfilePageView, *args, **kwargs)

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user']= page_user
        return context

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

class UserSettingsEditView(generic.UpdateView):
    form_class = EditUserSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserSettingsEditView, *args, **kwargs)
  

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/my_login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        return get_category_menu_context(self, UserLoginView, *args, **kwargs)
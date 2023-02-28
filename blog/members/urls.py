from django.urls import path
from .views import password_success

from .views import (
    UserRegisterView,
    UserLoginView,
    UserSettingsEditView,
    PasswordsChangeView,
    ShowProfilePageView,
    EditProfilePageView,
    CreateProfilePageView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserSettingsEditView.as_view(), name='edit_settings'),
    path('my_login/', UserLoginView.as_view(), name='my_login'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
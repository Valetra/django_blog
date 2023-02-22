from django.urls import path
from .views import UserRegisterView, UserLoginView, UserEditView, PasswordsChangeView
from .views import password_success

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('my_login/', UserLoginView.as_view(), name='my_login'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', password_success, name='password_success'),
]
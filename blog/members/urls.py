from django.urls import path
from .views import UserRegisterView, UserLoginView, UserEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('my_login/', UserLoginView.as_view(), name='my_login'),
]
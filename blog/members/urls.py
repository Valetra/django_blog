from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('my_login/', UserLoginView.as_view(), name='my_login'),
]
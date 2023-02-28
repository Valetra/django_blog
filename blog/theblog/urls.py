from django.urls import path
from .views import (
    HomeView, 
    ArticleDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    LikeView,
    AddCommentView,
    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artile/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]
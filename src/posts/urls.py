from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete
from django.contrib.auth.decorators import login_required
app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', login_required(BlogPostCreate.as_view()), name="Create"),
    path('edit/<str:slug>', BlogPostUpdate.as_view(), name="Edit"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="Post"),
    path('delete/<str:slug>', BlogPostDelete.as_view(), name="Delete")
]

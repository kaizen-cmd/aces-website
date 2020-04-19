from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.blogindex, name="blog-index"),
    path('posts/<slug:blog_title>/', views.viewblog, name="blogpost")
]
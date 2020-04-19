from django.shortcuts import render, HttpResponse
from . import models

def blogindex(request):
    blogs = models.BlogPosts.objects.all()
    return render(request, 'blogindex.html', {'blogs': blogs})

def viewblog(request, blog_title):
    blog = models.BlogPosts.objects.filter(title=blog_title)
    disp_blog = None
    for i in blog:
        disp_blog = i
    return render(request, "blog.html", {'blog': disp_blog})

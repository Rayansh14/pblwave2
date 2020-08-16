from django.shortcuts import render, get_object_or_404
from .models import Blog


def allBlogs(request):
    blogs = Blog.objects.all()
    return render(request, 'allBlogs.html', {'blogs': blogs})


def detail(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    return render(request, 'detail.html', {'blog': blog})

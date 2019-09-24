from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog_detail})

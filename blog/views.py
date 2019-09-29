from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	blogs = Blog.objects.order_by('-pub_date')
	return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog_detail(request, blog_title):
	unslug_title = blog_title.replace('-', ' ')
	blog_detail = get_object_or_404(Blog, title=unslug_title)
	return render(request, 'blog/blog_detail.html', {'blog': blog_detail})

def blog_tags(request, blog_tag):
	search_tag = blog_tag.replace('-', ' ')
	blogs = Blog.objects.filter(tags__icontains=search_tag).order_by('-pub_date')
	return render(request, 'blog/blogs.html', {'blogs': blogs})
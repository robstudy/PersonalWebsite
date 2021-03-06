from django.shortcuts import render, get_object_or_404
from .models import Blog
#for json response
from django.core import serializers
from django.http import HttpResponse
#Q allows or/and queries 
from django.db.models import Q
#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def allblogs(request):
	blogs = Blog.objects.order_by('-pub_date')
	page = request.GET.get('page', 1)

	#set limit per page
	paginator = Paginator(blogs, 10)

	try:
		return_blogs = paginator.page(page)
	except PageNotAnInteger:
		return_blogs = paginator.page(1)
	except EmptyPage:
		return_blogs = paginator.page(paginator.num_pages)

	return render(request, 'blog/blogs.html', {'blogs': return_blogs})

def blog_detail(request, blog_title):
	blog_detail = get_object_or_404(Blog, slug_name=blog_title)
	return render(request, 'blog/blog_detail.html', {'blog': blog_detail})

def blog_tags(request, blog_tag):
	search_tag = blog_tag.replace('-', ' ')
	blogs = Blog.objects.filter(tags__icontains=search_tag).order_by('-pub_date')
	return render(request, 'blog/blogs.html', {'blogs': blogs})

def get_all_blogs_serialized(request):
	blogs = Blog.objects.order_by('-pub_date')
	serialized_blogs = serializers.serialize('json', blogs)
	return HttpResponse(serialized_blogs, content_type="text/json-comment-filtered")

def get_filtered_blogs(request):
	if request.GET.get('terms'):
		filtered = request.GET['terms']
		blogs = Blog.objects.filter(Q(title__icontains=filtered) | Q(tags__icontains=filtered)).order_by('-pub_date')
		return render(request, 'blog/blogs.html', {'blogs': blogs})
	else:
		blogs = Blog.objects.order_by('-pub_date')
		return render(request, 'blog/blogs.html', {'blogs': blogs})
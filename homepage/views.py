from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def homepage(request):
	blogs = Blog.objects.order_by('-pub_date')
	return render(request, 'homepage.html', {'blogs': blogs})

def about(request):
	return render(request, 'about.html')
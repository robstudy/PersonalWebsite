from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from projects.models import Project

def homepage(request):
	blogs = Blog.objects.order_by('-pub_date')
	projects = Project.objects.order_by('-pub_date')
	return render(request, 'homepage/homepage.html', {'blogs': blogs, 'projects': projects})

def about(request):
	return render(request, 'homepage/about.html')
from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
	projects = Project.objects.order_by('-pub_date')
	return render(request, 'projects/projects.html', {'projects': projects})

def project_detail(request, project_name):
	project = get_object_or_404(Project, slug_name=project_name)
	return render(request, 'projects/project_detail.html', {'project': project})
from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
	return render(request, 'projects/projects.html')

def project_detail(request, project_name):
	name = project_name.replace('-', ' ')
	project = get_object_or_404(Project, title=name)
	return render(request, 'projects/project_detail.html', {'project': project})



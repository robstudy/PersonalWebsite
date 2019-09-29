"""TheFifthMoon URL Configuration
"""
from django.contrib import admin
from django.urls import path
from homepage import views as hm_view
from blog import views as blog_view
from projects import views as projects_view
from django.conf.urls.static import static
from django.conf import settings
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hm_view.homepage, name='homepage'),
    path('blog/', blog_view.allblogs, name='allblogs'),
    path('about/', hm_view.about, name='about'),
    path('projects/', projects_view.projects, name='projects'),
    path('projects/<slug:project_name>/', projects_view.project_detail, name="project_detail"),
    path('blog/<slug:blog_title>/', blog_view.blog_detail, name="blog_detail"),
    path('blogs/tag/<slug:blog_tag>/', blog_view.blog_tags, name="blog_tag"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

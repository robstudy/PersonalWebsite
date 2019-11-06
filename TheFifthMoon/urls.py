"""TheFifthMoon URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from homepage import views as hm_view
from blog import views as blog_view
from blog.api_views import BlogList
from projects import views as projects_view

import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hm_view.homepage, name='homepage'),
    path('blog/', blog_view.allblogs, name='allblogs'),
    path('api/v1/blogs/', BlogList.as_view()),
    path('about/', hm_view.about, name='about'),
    path('projects/', projects_view.projects, name='projects'),
    path('projects/<slug:project_name>/', projects_view.project_detail, name="project_detail"),
    path('blog/<slug:blog_title>/', blog_view.blog_detail, name="blog_detail"),
    path('blogs/tag/<slug:blog_tag>/', blog_view.blog_tags, name="blog_tag"),
    path('blogs/query/', blog_view.get_filtered_blogs, name="blog_filter"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

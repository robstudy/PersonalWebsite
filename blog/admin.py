from django.contrib import admin
from .models import Blog
from .forms import BlogForm

admin.site.register(Blog)
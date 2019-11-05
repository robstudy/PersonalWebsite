from rest_framework import generics

from blog.serializers import BlogSerializer
from blog.models import Blog

class BlogList(generics.ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
from rest_framework import generics

from blog.serializers import BlogSerializer
from blog.models import Blog

class BlogList(generics.ListAPIView):
	queryset = Blog.objects.order_by('-pub_date')
	serializer_class = BlogSerializer
from rest_framework import serializers

from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ('id', 'title', 'slug_name', 'tags', 'pub_date', 'body')

	def to_representation(self, instance):
		data = super().to_representation(instance)
		data['pub_date_pretty'] = instance.pub_date_pretty()
		data['summary'] = instance.summary()
		data['get_image_name'] = instance.get_image_name()
		return data
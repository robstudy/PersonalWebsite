from django.db import models
import re

class Blog(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
 
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
    def all_tags(self):
    	tag_list = re.split(',', self.tags)
    	for i in range(len(tag_list)):
    		tag_list[i] = tag_list[i].strip()
    	return tag_list
    def contains_tag(self, tag_term):
    	alltags = self.all_tags()
    	return tag_term in alltags
    def get_image_name(self):
    	#reference static/images for list
    	alltags = self.all_tags()
    	if 'c++' in alltags:
    		return 'cpp_logo.png'
    	elif 'python' in alltags:
    		return 'python.png'
    	elif 'javascript' in alltags:
    		return 'js.png'
    	elif 'book' in alltags:
    		return 'book.jpg'
    	else:
    		return 'random.png'
    def __str__(self):
        return self.title
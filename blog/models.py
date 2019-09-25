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
    def __str__(self):
        return self.title
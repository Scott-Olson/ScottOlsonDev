from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=30, unique=True)

	class  Meta:
		ordering = ['name']

	def __str__(self):
		return self.name 

def upload_location(instance, filename):
	file_name = str(filename)
	post_id = str(instance.slug)
	file_str = post_id + "/" + file_name
	return file_str


class Blog(models.Model):
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	updated_on = models.DateTimeField(auto_now=True)
	summary = models.CharField(max_length=250, unique=False)
	content = MarkdownxField()
	thumbnail = models.ImageField(
		 upload_to=upload_location,
		 width_field = "width_field", 
		 height_field="height_field"
		 )
	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	created_on = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, related_name='blogs')

	class Meta:
		ordering = ['-updated_on']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# print("forming the absolute url")
		return reverse("detail", kwargs={"slug":self.slug})

	def get_thumbnail_url(self):
		test = "http://127.0.0.1:8000/media/"
		return test

from django.shortcuts import render
from django.http import Http404
from .models import Blog, Tag
# Create your views here.

def landing(request):
	queryset = Blog.objects.all().order_by('-updated_on')
	context = {'blog_list': queryset}
	return render(request, 'blog_landing.html', context = context)


def get_blog_by_id(request, id):
	try:
		query = Blog.objects.filter(id = id)
	except:
		raise 'Blog with that ID not found'
	pass

def get_blog_by_slug(request, slug):
	print(slug)
	try:
		query = Blog.objects.filter(slug = slug).order_by('-created_on')
	except Blog.DoesNotExist:
		raise Http404('Blog entry not found.')
	return render(request, 'blog_page.html', {'blog': query})

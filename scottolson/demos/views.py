from django.shortcuts import render, HttpResponse

# Create your views here.

def landing(request):
	return HttpResponse("Demos for now")
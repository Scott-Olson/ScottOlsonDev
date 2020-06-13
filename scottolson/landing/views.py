from django.shortcuts import render

from django.core.mail import send_mail
import os


# Create your views here.
def index(request):

	send_mail("TEST AGAIN", "This is using dotenv", os.getenv('DEV_EMAIL'), [os.getenv('DEV_EMAIL')])

	return render(request, 'index.html')

from django.http import HttpResponse 
from django.shortcuts import render

from .models import *
# Create your views here.

"""def index(request):

	return HttpResponse("Hello World and Andrey!!!")"""

def index(request):
	return render (request, 'products/index.html',)
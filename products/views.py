from django.http import HttpResponse 

from .models import *
# Create your views here.

"""def index(request):

	return HttpResponse("Hello World and Andrey!!!")"""

def searchProducts(request):
	return render (request, 'search.html',{})
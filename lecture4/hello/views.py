from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "hello/index.html")

def carlo(request):
	return HttpResponse("hello, Carlo!")

def david(request):
	return HttpResponse("hello, David!")

def greet(request, name):
	return render(request, "hello/greet.html", 
	{ "name": name.capitalize() 
	})

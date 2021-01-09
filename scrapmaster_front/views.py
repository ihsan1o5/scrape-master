from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'frontend/index.html')

def services(request):
	return render(request, 'frontend/services.html')

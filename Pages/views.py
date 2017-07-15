from django.shortcuts import render



def index(request):
	context={}
	return render(request, 'Pages/index.html', context)

def about(request):
	context={}
	return render(request, 'Pages/about.html', context)
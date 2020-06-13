from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request, 'Home.html')

def login_f(request):
	return HttpResponse("hello ,world")

def page2(request):
	return render(request,'page2.html')

def page1(request):
	return render(request,'page1.html')

#csrf_exempt
def submit_form(request):
	username1=request.GET['uname']
	password1=request.GET['pword']
	if (username1=='shabbirsaifee' and password1== '1234'):
		return render(request,'page2.html')
	else:
		return HttpResponse("Who are you")

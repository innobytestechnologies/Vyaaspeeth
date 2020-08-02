from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render

# Create your views here.
def home_live(request):
	"""the homepage view"""
	context = {}
	template = 'home_live.html'
	return render(request,template,context)

def about(request):
	"""about page"""
	context = {}
	template = 'about_live.html'
	return render(request,template,context)

@login_required
def dashboard(request):
	"""about page"""
	context = {'user':request.user}
	template = 'dashboard_live.html'
	return render(request,template,context)



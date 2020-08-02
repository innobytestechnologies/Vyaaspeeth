from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
@login_required(login_url=reverse_lazy('accounts:login'))
def home(request):
	"""the homepage view"""
	context = {}
	template = 'home_live.html'
	return render(request,template,context)

def about(request):
	"""about page"""
	context = {}
	template = 'about.html'
	return render(request,template,context)

@login_required
def dashboard(request):
	"""about page"""
	context = {'user':request.user}
	template = 'dashboard.html'
	return render(request,template,context)

def auditions(request):
	context = {}
	template = 'dist/index.html'
	return render(request, template, context)

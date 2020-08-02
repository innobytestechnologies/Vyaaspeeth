from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.core.mail import send_mail

from .forms import BookLiveForm
import datetime



def show_index(request):
	movie_list = Movie.objects.all().order_by('popularity_index')
	top_movie = Movie.objects.all().order_by('popularity_index')[:3]

	return render(request, 'common_live/booking.html', {'movie_list': movie_list,
		'top_movie': top_movie})

def movie_list(request):
	movies = Movie.objects.all().order_by('language')
	movie_list = []
	movie_by_lang = []
	lang = movies[0].language
	for i in range(0, len(movies)):
		if lang != movies[i].language:
			lang = movies[i].language
			movie_list.append(movie_by_lang)
			movie_by_lang = []
		movie_by_lang.append(movies[i])

	movie_list.append(movie_by_lang)

	return render(request, 'movie/movie_list.html', {'movies': movie_list})


def movie_details(request, movie_id):
	try:
		movie_info = Movie.objects.get(pk=movie_id)
		shows = Show.objects.filter(movie=movie_id,
			date=datetime.date.today()).order_by('theatre')
		show_list = []
		show_by_theatre = []
		theatre = shows[0].theatre
		for i in range(0, len(shows)):
			if theatre != shows[i].theatre:
				theatre = shows[i].theatre
				show_list.append(show_by_theatre)
				show_by_theatre = []
			show_by_theatre.append(shows[i])

		show_list.append(show_by_theatre)

	except Movie.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'movie/movie_details.html',
		{'movie_info': movie_info, 'show_list': show_list})


def theatre_list(request):
	theatres = Theatre.objects.all().order_by('city')
	theatre_list = []
	theatre_by_city = []
	city = theatres[0].city
	for i in range(0, len(theatres)):
		if city != theatres[i].city:
			city = theatres[i].city
			theatre_list.append(theatre_by_city)
			theatre_by_city = []
		theatre_by_city.append(theatres[i])

	theatre_list.append(theatre_by_city)

	return render(request, 'theatre_live/theatre_list.html', {'theatres': theatre_list})


def theatre_details(request, theatre_id):
	try:
		theatre_info = Theatre.objects.get(pk=theatre_id)
		shows = Show.objects.filter(theatre=theatre_id,
			date=datetime.date.today()).order_by('movie')

		show_list = []
		show_by_movie = []
		movie = shows[0].movie
		for i in range(0, len(shows)):
			if movie != shows[i].movie:
				movie = shows[i].movie
				show_list.append(show_by_movie)
				show_by_movie = []
			show_by_movie.append(shows[i])

		show_list.append(show_by_movie)

		print(show_list)

	except Theatre.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'theatre/theatre_details.html',
		{'theatre_info': theatre_info, 'show_list': show_list})


def book_live_view(request):
	global form
	if request.POST:
		print('HI')
		form=BookLiveForm(request.POST)
		print("HI AGAIN")
		if form.is_valid():
			print("HI IF VALID")
			global booking_details
			booking_details=form.save(commit=False)
			booking_details.save()
			print(booking_details)
			return redirect('booking_confirmation')
	else:
		form  = BookLiveForm()
	context = {
        	"form":form,
     	}
	return render(request, 'booking_live/book_live.html',context=context)


def booking_confirmation(request):
	print(form.is_valid())
	print(form.errors)
	
	instance=book_live.objects.all().order_by('-id')[0]
	print(instance)
	context={
	    "visitor":instance
	}
	return render(request, 'booking_live/booking_confirmation.html',context=context)



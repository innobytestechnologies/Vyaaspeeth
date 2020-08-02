from django.contrib import admin

# Register your models here.
from .models import Movie,Show,Event,book_live

class ShowAdmin(admin.ModelAdmin):
	class Meta:
		model = Show

admin.site.register(Show,ShowAdmin)

class MovieAdmin(admin.ModelAdmin):
	class Meta:
		model = Movie

admin.site.register(Movie,MovieAdmin)

class BookLive(admin.ModelAdmin):
	class Meta:
		model = book_live

admin.site.register(book_live,BookLive)

class EventAdmin(admin.ModelAdmin):
	class Meta:
		model = Event

admin.site.register(Event,EventAdmin)

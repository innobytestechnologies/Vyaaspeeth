from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
#from django.core.validators import validate_comma_separated_integer_list
import datetime

# Create your models here.

class Movie(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    rating_choice = (
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),
    )
    name = models.CharField(max_length=20,null=True,blank=True)
    cast = models.CharField(max_length=100,null=True,blank=True)
    director = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)
    certificate = models.CharField(max_length=2, choices=rating_choice)
    popularity_index = models.IntegerField(unique=True, null=True, blank=True)
    trailer = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.IntegerField(default=1)
    date = models.DateField()

    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + str(self.theatre) + "-" + str(self.date) + "-" + str(self.time)



def show_index(request):
    movie_list = Movie.objects.all().order_by('popularity_index')
    top_movie = Movie.objects.all().order_by('popularity_index')[:3]
    return render(request, 'common/booking.html', {'movie_list': movie_list,'top_movie': top_movie})


class Event(models.Model):
    lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    name = models.CharField(max_length=20,null=True,blank=True)
    price = models.IntegerField(null=True,blank = True)
    cast = models.CharField(max_length=100,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    def __str__(self):
        return str(self.name) + '|' + str(self.cast)



class book_live(models.Model):
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )


    name = models.CharField(max_length = 500,null=True,blank=True)
    age=models.IntegerField(null=True,blank = True)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    event=models.ForeignKey(Event, on_delete = models.CASCADE)
    mobile = models.BigIntegerField(null=True,blank=True)
    email_id=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return str(self.name)



    




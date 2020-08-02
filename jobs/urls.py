from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static #for static files on local server.
from django.conf.urls import include
from django.views.generic import TemplateView

from dashboard import views as dash_views
from contact import views as cont_views
from checkout import views as check_views
from booking import views as booking_views

from dashboard_live import views as dash_views_live
from contact_live import views as cont_views_live
from checkout_live import views as check_views_live
from booking_live import views as booking_views_live


from accounts.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Jobs Portal API",
      default_version='v1',
      description="Jobs Portal Api Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
    path('api/', include([
        path('swagger', schema_view.with_ui('swagger', cache_timeout=0)),
        path('', include('accounts.api.urls')),
        path('', include('jobsapp.api.urls')),
    ])), 
    url(r'^accounts/login/$',LoginView.as_view(), name='login'),
    url(r'^todo/', include('todo.urls', namespace="todo")),
    url(r'^aud_exhibit/$',dash_views.auditions, name = 'auditions'),
    url(r'^bookshow/$', dash_views.home, name='home'),
    url(r'^bookshow/dashboard/$', dash_views.dashboard,name='dashboard'),
    url(r'^bookshow/contact/$', cont_views.contact,name='contact'),
    url(r'^bookshow/accounts/', include('allauth.urls')),
    #url(r'^booking/$', booking_views.movie_list, name='movie_list'),
    url(r'^bookshow/booking/$', booking_views.show_index,name='booking'),
    url(r'^bookshow/checkout/$', check_views.checkout,name='checkout'),
    url(r'^bookshow/booking/(?P<movie_id>\d+)/$', booking_views.movie_details, name='movie_details'),
    url(r'^bookshow/booking/seatchoice/(?P<show_id>\d+)/$', booking_views.reserve_seat, name='reserve_seat'),
    url(r'^bookshow/booking/payment/$', booking_views.payment_gateway, name='payment_gateway'),
    url(r'^bookshow/booking/payment_confirmation/$', booking_views.payment_confirmation, name='payment_confirmation'),
    #Hard Coded templates i.e. without views.
    url(r'^bookshow/booking/payment/booking/seatnotfound.html$', TemplateView.as_view(template_name="booking/seatnotfound.html"), name='seatnotfound'),
    url(r'^bookshow/booking/payment_confirmation/booking/seatconflict.html$', TemplateView.as_view(template_name="booking/seatconflict.html"), name='seatconflict'),
    url(r'^vyas_live/$', dash_views_live.home_live, name='home_live'),
    url(r'^vyas_live/dashboard_live/$', dash_views_live.dashboard,name='dashboard_live'),
    url(r'^vyas_live/contact_live/$', cont_views_live.contact,name='contact_live'),
    url(r'^vyas_live/accounts_live/', include('allauth.urls')),
    #url(r'^booking/$', booking_views.movie_list, name='movie_list'),
    url(r'^vyas_live/booking_live/$', booking_views_live.show_index,name='booking_live'),
    url(r'^vyas_live/checkout_live/$', check_views_live.checkout,name='checkout_live'),
    url(r'^vyas_live/booking_live/(?P<movie_id>\d+)/$', booking_views_live.movie_details, name='movie_details'),
    url(r'^vyas_live/booking_live/book_live/$', booking_views_live.book_live_view, name='book_live_view'),
    url(r'^vyas_live/booking_live/book_live/booking_confirmation/$', booking_views_live.booking_confirmation, name='booking_confirmation'),
    

]

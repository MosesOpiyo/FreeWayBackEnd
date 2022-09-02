from django.urls import path
from FreeWayVenues import views as venue_views

urlpatterns = [
     path('user_profile',venue_views.venue_view,name='profile'),
]
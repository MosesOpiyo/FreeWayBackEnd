from django.urls import path
from FreeWayVenues import views as venue_views

urlpatterns = [
     path('venues',venue_views.venue_view,name='venues'),
     path('venue/<int:pk>',venue_views.singleVenue,name='venue'),
]
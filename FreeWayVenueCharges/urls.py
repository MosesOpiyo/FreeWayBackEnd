from django.urls import path
from FreeWayVenueCharges import views as charges_views

urlpatterns = [
    path('venue_charges',charges_views.charges_view,name='venue_charges')
]
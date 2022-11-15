from django.urls import path
from VenueBarriers import views as user_views

urlpatterns = [
     path('all_barriers',user_views.all_barriers,name='barriers'),
]
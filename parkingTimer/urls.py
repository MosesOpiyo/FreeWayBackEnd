from django.urls import path
from parkingTimer import views as user_views

urlpatterns = [
     path('activate',user_views.activateTimer,name='activate'),
]
from django.urls import path
from UserInstance import views as user_views

urlpatterns = [
     path('user_profile',user_views.user_profile,name='profile'),
]
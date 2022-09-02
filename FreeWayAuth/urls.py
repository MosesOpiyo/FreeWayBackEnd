from django.urls import path
from FreeWayAuth import views as Authenticated_users
from rest_framework.authtoken import views as special_views

urlpatterns = [
    path('registration', Authenticated_users.registration_view,name="registration"),
    path('login', special_views.obtain_auth_token),
]
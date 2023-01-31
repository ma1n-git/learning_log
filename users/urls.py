"""Defines URL patterns for learning_log. Main URL's """

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Add installed (by Django) URL auth.
    path('', include('django.contrib.auth.urls'))
]

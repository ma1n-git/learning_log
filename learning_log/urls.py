"""Defines URL patterns for learning_log. Main URL's """
from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('register', views.register, name='register'),
    path('', include('learning_logs.urls')),
]

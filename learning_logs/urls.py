"""Defines URL patterns for learning_logs. """

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Main page.
    path('', views.main, name='main'),
    # All the topics.
    path('topics/', views.topics, name='topics'),
    # A topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]

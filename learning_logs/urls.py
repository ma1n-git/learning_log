"""Defines URL patterns for learning_logs. """

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Main page.
    path('', views.main, name='main'),
    # All the topics.
    path('topics/', views.topics, name='topics'),
    # A certain topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Adding a new topic
    path('new_topic/', views.new_topic, name='new_topic')
]

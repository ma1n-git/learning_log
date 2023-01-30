from django.contrib import admin

from .models import Topic, Entry

"""Registering models in admin site."""
admin.site.register(Topic)
admin.site.register(Entry)

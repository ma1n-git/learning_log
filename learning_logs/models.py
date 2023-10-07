from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """Article which is learnt by user."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return string name of model."""
        return self.text


class Entry(models.Model):
    """Some certain info about this article"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Plural name of class."""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return view of model in String."""
        return f"{self.text[:50]}..."
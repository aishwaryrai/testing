from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    registered_users = models.ManyToManyField(User, blank=True, related_name='registered_events')

    def __str__(self):
        return self.title

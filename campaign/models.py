from django.db import models
from django.conf import settings

class Campaign (models.Model):

    title = models.TextField(unique=True)
    description = models.TextField()
    campImage = models.ImageField()
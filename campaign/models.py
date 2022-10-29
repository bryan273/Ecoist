from django.db import models
from django.conf import settings

class Campaign (models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True,)
    title = models.TextField()
    description = models.TextField()
    campImage = models.ImageField()
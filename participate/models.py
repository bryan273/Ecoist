
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_pendaftar = models.CharField(max_length=50)
    email_pendaftar = models.CharField(max_length=50)
    phone_number = models.IntegerField()
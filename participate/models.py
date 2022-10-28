
from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Participants(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_pendaftar = models.CharField(max_length=50, default='')
    email_pendaftar = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=15, default='0')
    what_can_you_help_with = models.CharField(max_length=50, verbose_name='What can you help with?', default="")
    reason_to_participate = models.CharField(max_length=500, default='')
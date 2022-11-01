from django.db import models
from django.contrib.auth.models import User
from campaign.models import Campaign
# Create your models here.
class Donasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='title', default=None, null=True)
    nominal = models.IntegerField()
    jumlahPohon = models.IntegerField()
    namaPohon = models.CharField(max_length=255)
    pesan = models.TextField()
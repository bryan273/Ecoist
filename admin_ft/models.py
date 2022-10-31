from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class admin_ft_entry(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=30, default='-') 
    noted = models.TextField(default='-')

# class merge(models.Model):
#     username = models.CharField(max_length=30, default='-') 
#     nominal = models.IntegerField()
#     jumlahPohon = models.IntegerField()
#     namaPohon = models.CharField(max_length=255)
#     pesan = models.TextField()
#     title = models.TextField()
#     description = models.TextField()


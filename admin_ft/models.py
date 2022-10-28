from django.db import models
from django.contrib.auth.models import User

class admin_ft_entry(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=30, default='-') 
    nominal_uang = models.BigIntegerField(default=0)
    jumlah_pohon = models.IntegerField(default=0)
    pesan = models.TextField(default='-')
    # payment_method = models.CharField(max_length=50, default='-')
    # unit_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # date = models.DateField()
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    # is_finished = models.BooleanField(default=False, null=True, blank=True)


from django.db import models

# Create your models here.


class Scripts(models.Model):
    token = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    expiry = models.CharField(max_length=100, default=None, blank=True, null=True)
    strike = models.CharField(max_length=100)
    lotsize = models.CharField(max_length=100)
    instrumenttype = models.CharField(max_length=100, default=None, blank=True, null=True)
    exch_seg = models.CharField(max_length=100)
    tick_size =  models.CharField(max_length=100)

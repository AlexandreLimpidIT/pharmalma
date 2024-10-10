from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    cis_code = models.CharField(max_length=8, default="00000000")
    cip_code = models.CharField(max_length=13, default="1234567")

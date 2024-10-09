from django.db import models
from .phamacies import Pharmacies

class Horiares(models.Model):

    id_pharma=models.ForeignKey(Pharmacies,on_delete=models.CASCADE)
    jour=models.CharField(max_length=8)
    periode=models.CharField(max_length=5)
    h_debut=models.TimeField()
    h_fin=models.TimeField()
    class Meta:
        db_table="Horaires"
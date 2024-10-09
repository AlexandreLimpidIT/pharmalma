from django.db import models
from .phamacies import Pharmacies
from .medicaments import Medicaments

class Stocks(models.Model):
    ref_medoc=models.ForeignKey(Medicaments,on_delete=models.CASCADE,db_index=True)
    id_pharma=models.ForeignKey(Pharmacies,on_delete=models.CASCADE,db_index=True)
    qte=models.FloatField()
    class Meta:
        db_table="Stocks"
from django.db import models
from .phamacies import Pharmacie
from .medicaments import Medicament

class Stock(models.Model):
    ref_medoc=models.ForeignKey(Medicament,on_delete=models.CASCADE,db_index=True)
    id_pharma=models.ForeignKey(Pharmacie,on_delete=models.CASCADE,db_index=True)
    qte=models.FloatField()
    class Meta:
        db_table="Stocks"
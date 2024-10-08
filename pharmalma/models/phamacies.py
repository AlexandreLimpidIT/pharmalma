from django.db import models
from django.contrib.auth.models import User

class Pharmacie(models.Model):
    id_pharma=models.AutoField(primary_key=True, unique=True)
    nom_pharma=models.CharField(max_length=30)
    adresse_pharma=models.CharField(max_length=150)
    telephone=models.FloatField()
    id_pharmacien=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="Pharmacies"
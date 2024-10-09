from django.db import models

class Medicaments(models.Model):
    ref_medoc=models.CharField(primary_key=True,max_length=15)
    nom_medoc=models.CharField(max_length=20)
    class Meta:
        db_table="Medicaments"
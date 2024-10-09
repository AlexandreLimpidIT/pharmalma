# pharmalma/admin.py

from django.contrib import admin
from .models import Horaire,Medicament,Pharmacie,Stock


@admin.register(Horaire)
class HoraireAdmin(admin.ModelAdmin):
    list_display = ('id_pharma', 'jour', 'periode','h_debut','h_fin')  
    search_fields = ('id_pharma', 'jour', 'periode','h_debut','h_fin')
@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('ref_medoc', 'nom_medoc')  
    search_fields = ('ref_medoc', 'nom_medoc')
@admin.register(Pharmacie)
class PharmacieAdmin(admin.ModelAdmin):
    list_display = ('id_pharma', 'nom_pharma', 'adresse_pharma','telephone','id_pharmacien')
    search_fields = ('id_pharma', 'nom_pharma', 'adresse_pharma', 'telephone','id_pharmacien')

@admin.register(Stock)
class PharmacieAdmin(admin.ModelAdmin):
    list_display = ('ref_medoc', 'id_pharma', 'qte')
    search_fields = ('ref_medoc', 'id_pharma', 'qte')
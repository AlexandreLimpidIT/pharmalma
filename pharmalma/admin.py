# pharmalma/admin.py

from django.contrib import admin
from .models import Product,Horiares,Medicaments,Pharmacies,Stocks

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cis_code', 'cip_code')  # Champs à afficher dans la liste
    search_fields = ('name', 'cis_code', 'cip_code')         # Champ de recherche

@admin.register(Horiares)
class HoraireAdmin(admin.ModelAdmin):
    list_display = ('id_pharma', 'jour', 'garde','periode','h_debut','h_fin')  
    search_fields = ('id_pharma', 'jour', 'garde','periode','h_debut','h_fin')
@admin.register(Medicaments)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('ref_medoc', 'nom_medoc')  
    search_fields = ('ref_medoc', 'nom_medoc')
@admin.register(Pharmacies)
class PharmacieAdmin(admin.ModelAdmin):
    list_display = ('id_pharma', 'nom_pharma', 'adresse_pharma','latitude','longitude','telephone','id_pharmacien')
    search_fields = ('id_pharma', 'nom_pharma', 'adresse_pharma', 'latitude', 'longitude', 'telephone','id_pharmacien')

@admin.register(Stocks)
class PharmacieAdmin(admin.ModelAdmin):
    list_display = ('ref_medoc', 'id_pharma', 'qte')
    search_fields = ('ref_medoc', 'id_pharma', 'qte')
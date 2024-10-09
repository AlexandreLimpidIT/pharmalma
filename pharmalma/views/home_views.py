from django.shortcuts import render
from django.http import JsonResponse
from ..models import Pharmacie, Stock, Medicament
import requests

def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('medicament')  # Récupère le nom du médicament
        pharmacies_info = []  # Liste pour stocker les informations des pharmacies

        # Recherche les produits qui correspondent au nom donné
        products = Medicament.objects.filter(nom_medoc__icontains=product_name)

        # Recherche les pharmacies ayant ces produits en stock
        for product in products:
            stock_entries = Stock.objects.filter(ref_medoc=product.ref_medoc)
            for stock in stock_entries:
                if stock.qte != 0:
                    pharmacy = Pharmacie.objects.get(id_pharma=stock.id_pharma.id_pharma)
                    adresse = pharmacy.adresse_pharma
                    
                    # Appel à l'API Google Geocoding pour obtenir la latitude et la longitude
                    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={adresse}&key=AIzaSyDq4tK0ZwN8tu9ZQgF6Y3TJ2EPScOCSULk')
                    if response.status_code == 200:
                        data = response.json()
                        if data['results']:
                            location = data['results'][0]['geometry']['location']
                            lat = location['lat']
                            lng = location['lng']
                            pharmacies_info.append({
                                'adresse': adresse,
                                'nom': pharmacy.nom_pharma,  # Assurez-vous que ce champ existe
                                'telephone': pharmacy.telephone,  # Assurez-vous que ce champ existe
                                'lat': lat,
                                'lng': lng
                            })

        return JsonResponse({'pharmacies': pharmacies_info})

    return render(request, 'home.html')
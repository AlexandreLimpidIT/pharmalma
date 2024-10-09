from django.shortcuts import render
from django.http import JsonResponse
from ..models import Pharmacie, Stock, Medicament

def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('medicament')  # Récupère le nom du médicament
        addresses = []

        # Recherche les produits qui correspondent au nom donné
        products = Medicament.objects.filter(nom_medoc__icontains=product_name)

        # Recherche les pharmacies ayant ces produits en stock
        for product in products:
            stock_entries = Stock.objects.filter(ref_medoc=product.ref_medoc)
            for stock in stock_entries:
                if(stock.qte != 0):
                    print(f"ID pharmacie : {stock.id_pharma.id_pharma}")
                    pharmacy = Pharmacie.objects.filter(id_pharma=stock.id_pharma.id_pharma)
                    for i in pharmacy :
                        addresses.append(i.adresse_pharma)

        print(addresses)

        return JsonResponse({'addresses': addresses})
    return render(request, 'home.html')

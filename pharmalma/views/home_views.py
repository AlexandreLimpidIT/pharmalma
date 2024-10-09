from django.shortcuts import render
from django.http import JsonResponse
from ..models import Pharmacie, Product, Stock

def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('medicament')  # Récupère le nom du médicament
        addresses = []

        # Recherche les produits qui correspondent au nom donné
        products = Product.objects.filter(name__icontains=product_name)

        # Recherche les pharmacies ayant ces produits en stock
        for product in products:
            stock_entries = Stock.objects.filter(id_prod=product.id)
            for stock in stock_entries:
                if(stock.quantite != 0):
                    print(f"ID pharmacie : {stock.id_pharma}")
                    pharmacy = Pharmacie.objects.filter(id=stock.id_pharma)
                    for i in pharmacy :
                        addresses.append(i.adresse)

        print(addresses)

        return JsonResponse({'addresses': addresses})
    return render(request, 'home.html')

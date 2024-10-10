from django.shortcuts import render, redirect, get_object_or_404
from ..models import Horaire, Pharmacie, Medicament, Stock
from ..forms import HoraireForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect 

def pharmacienV(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, id_pharma=pharmacie_id)
    medicaments=Medicament.objects.all()
    fragment=True
    medicamentsCon={'medicaments' :medicaments,
                    'fragment':fragment,
                    'pharmacie':pharmacie}
    return render(request, './templates/pharmacie.html',medicamentsCon)

def horairePH(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, id_pharma=pharmacie_id)
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    selected_jour = request.POST.get('jour', None)
    horaires = None

    # Si un jour a été sélectionné, récupérer les horaires correspondants
    if selected_jour:
        horaires = Horaire.objects.filter(id_pharma=pharmacie, jour=selected_jour)
    
    #print(horaires[0].h_debut)

    # Rendre la page avec les horaires existants
    return render(request, 'templates/horaireForm.html', {
        'pharmacie': pharmacie,
        'jours': jours,
        'selected_jour': selected_jour,
        'horaires': horaires,
    })

def modifier_horaire(request, pharmacie_id, horaire_id):
    horaire = get_object_or_404(Horaire, id=horaire_id)
    
    if request.method == 'POST':
        form = HoraireForm(request.POST, instance=horaire)
        if form.is_valid():
            form.save()
            messages.success(request, 'Horaire modifié avec succès.')
        else:
            messages.error(request, 'Erreur dans la modification de l\'horaire.')
    
    # Redirection après modification
    return redirect('horairePH', pharmacie_id=pharmacie_id)

def renderStockPh(request, pharmacie_id, ref_medoc):
    medicament = get_object_or_404(Medicament, ref_medoc=ref_medoc)
    pharmacie = get_object_or_404(Pharmacie, id_pharma=pharmacie_id)
    stock = get_object_or_404(Stock, id_pharma=pharmacie, ref_medoc=medicament)

    return render(request, './templates/stocksForm.html', {
        "medicament": medicament,
        "pharmacie": pharmacie,
        "stock": stock
    })

def updateStock(request, pharmacie_id, ref_medoc):
    if request.method == 'POST':
        # Récupérer la quantité soumise
        quantity = request.POST.get('quantity-input')
        print(request.POST)
        
        # Récupérer le stock correspondant
        stock = get_object_or_404(Stock, id_pharma__id_pharma=pharmacie_id, ref_medoc__ref_medoc=ref_medoc)
        
        # Mettre à jour la quantité
        stock.qte = quantity
        stock.save()
        
        # Rediriger vers la page de stock après la mise à jour
        return redirect('leMedoc', pharmacie_id=pharmacie_id, ref_medoc=ref_medoc)

    return redirect('leMedoc', pharmacie_id=pharmacie_id, ref_medoc=ref_medoc)

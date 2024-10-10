from django.shortcuts import render, redirect, get_object_or_404
from ..models import Horaire, Pharmacie, Medicament
from ..forms import HoraireForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect 

def pharmacienV(request, pharmacie_id):
    medicaments=Medicament.objects.all()
    fragment=True
    medicamentsCon={'medicaments' :medicaments,
                    'fragment':fragment}
    return render(request, './templates/pharmacie.html',medicamentsCon)

from django.shortcuts import render, get_object_or_404, redirect
from ..models import Pharmacie, Horaire
from ..forms import HoraireForm
from django.contrib import messages

def horairePH(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, id_pharma=pharmacie_id)
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
    selected_jour = request.POST.get('jour', None)
    horaires = None

    # Si un jour a été sélectionné, récupérer les horaires correspondants
    if selected_jour:
        horaires = Horaire.objects.filter(id_pharma=pharmacie, jour=selected_jour)
    
    print(horaires[0].h_debut)

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

def stockPH(request, pharmacie_id):
    ref_medoc=request.GET.get('ref_medoc')
    if ref_medoc:
        medicament=Medicament.objects.get(ref_medoc=ref_medoc)
        return render(request,'./templates/stocksForm.html',{"medicament":medicament})
    else:
        medicaments=Medicament.objects.all()
        return render(request,'./templates/stocksForm.html',{"medicaments":medicaments})

def renderStockPh(request,pharmacie_id,ref_medoc):
    medicament=Medicament.objects.get(ref_medoc=ref_medoc)
    return HttpResponseRedirect(f"{reverse("stockPh")}?ref_medoc={ref_medoc}")

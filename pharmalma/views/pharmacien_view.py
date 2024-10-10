from django.shortcuts import render
from ..models import Pharmacies,Product,Medicaments,Stocks,Horiares
from django.urls import reverse
from django.http import HttpResponseRedirect 

def pharmacienV(request):
    medicaments=Medicaments.objects.all()
    fragment=True
    medicamentsCon={'medicaments' :medicaments,
                    'fragment':fragment}
    return render(request, './templates/pharmacie.html',medicamentsCon)

def horairePH(request):
    return render(request,'./templates/horaireForm.html')

def stockPH(request):
    ref_medoc=request.GET.get('ref_medoc')
    if ref_medoc:
        medicament=Medicaments.objects.get(ref_medoc=ref_medoc)
        return render(request,'./templates/stocksForm.html',{"medicament":medicament})
    else:
        medicaments=Medicaments.objects.all()
        return render(request,'./templates/stocksForm.html',{"medicaments":medicaments})

def renderStockPh(request,ref_medoc):
    medicament=Medicaments.objects.get(ref_medoc=ref_medoc)
    return HttpResponseRedirect(f"{reverse("stockPh")}?ref_medoc={ref_medoc}")

def modifStock(request):
    medica=request.POST.get("ref_medoc")
    medicament=Medicaments.objects.filter(ref_medoc=medica).first()
    quantite=request.POST.get("qte")
    pharmacie=1
    pharmaFormStc=pharmaFormStc(ref_medoc=medicament,id_pharma=pharmacie,qte=quantite,)
    pharmaFormStc.save()
    return HttpResponseRedirect(reverse("stockPh"))
from django.shortcuts import render

def pharmacienV(request):
    return render(request, './templates/pharmacie.html')

def horairePH(request):
    return render(request,'./templates/horaireForm.html')

def stockPH(request):
    return render(request,'./templates/stocksForm.html')
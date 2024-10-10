from django import forms
from .models import Horaire

class HoraireForm(forms.ModelForm):
    class Meta:
        model = Horaire
        fields = ['h_debut', 'h_fin']
        widgets = {
            'h_debut': forms.TimeInput(attrs={'type': 'time'}),
            'h_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
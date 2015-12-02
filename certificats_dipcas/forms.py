from django import forms

class Formulari_Municipi(forms.Form):
    nom_del_municipi = forms.CharField(max_length=100, label='Nom del municipi')
    
from django import forms

class Formulari_Municipi(forms.Form):
    nom_del_municipi = forms.CharField(max_length=100, label='Nom del municipi')
    certificat = forms.FileField(label='Certificat en format binari')
    clau = forms.FileField(label='Clau privada')
    
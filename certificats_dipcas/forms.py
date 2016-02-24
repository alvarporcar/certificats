from django import forms

class FormCertificats(forms.Form):
    municipi = forms.CharField(max_length=100, label='Nom del municipi')
    certificat = forms.FileField(label='Certificat en format binari')
    clau = forms.FileField(label='Clau privada')


class FormMunicipi(forms.Form):
    municipi = forms.CharField(max_length=100, label='Nom del municipi')
    
    
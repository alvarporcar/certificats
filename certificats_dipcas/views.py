# -*- coding: utf-8 -*-
from django.shortcuts import render
from certificats_dipcas.forms import Formulari_Municipi
import os


def generar_contrasenya(request):
    """
    Script per a calcular la contrasenya d'un nom d'Ajuntament
    El primer argument es el nom de l'Ajuntament 
    """
    if request.method == 'POST':
        form = Formulari_Municipi(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data 
            dicc_vocals = {"a":5,"e":4,"i":3,"o":2,"u":1}
            nom_municipi = cd['nom_del_municipi']
            i=0
            contrasenya = ""
            while i < len(nom_municipi):
                if dicc_vocals.has_key(nom_municipi[i]):
                    lletra = dicc_vocals[nom_municipi[i]]
                    contrasenya = contrasenya + str(lletra)
                else:
                    posicio = ord(nom_municipi[i])
                    if posicio == 121:
                        contrasenya = contrasenya + chr(97)
                    elif posicio == 122:
                        contrasenya = contrasenya + chr(98)    
                    else: 
                        contrasenya = contrasenya + chr(posicio + 2)
                i = i + 1
            contrasenya = '_'+ contrasenya
            return render(request,'contrasenya.html',{'contrasenya':contrasenya}) 

    else:
        form = Formulari_Municipi() 
          
    return render(request, 'formulari_municipi.html', {'form': form}) 


def convertir_certificat(request):
    """
    Script per a convertir un certificat en format binari a format pfx
    """
    if request.method == 'POST':
        form = Formulari_Municipi(request.POST, request.FILES) 
        if form.is_valid():
            cd = form.cleaned_data 
            nom_municipi = cd['nom_del_municipi']
            os.system("openssl x509 -inform DER -in "+str(request.FILES['certificat'])+" -outform PEM -out "+ "sello_"+nom_municipi+".crt")
            os.system("openssl pkcs12 -export -inkey "+str(request.FILES['clau'])+" -CApath ./accv -in "+"sello_"+nom_municipi+".crt"+" -out "+"sello_"+nom_municipi+".pfx")
            
            return render(request,'certificat_convertit.html',{'nom_municipi':nom_municipi}) 

    else:
        form = Formulari_Municipi() 
          
    return render(request, 'formulari_municipi.html', {'form': form}) 
    
    

# -*- coding: utf-8 -*-
from django.shortcuts import render
from certificats_dipcas.forms import Formulari_Municipi

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

    
    

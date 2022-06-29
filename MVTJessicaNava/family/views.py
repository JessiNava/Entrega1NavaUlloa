#from typing_extensions import Self
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from family.models import familia_nava, hobbies, ubicacion
from family.forms import Hobbieformulario


# Create your views here.
def familia(self):
    miembro1= familia_nava(nombre="Edgar", parentesco="Esposo", edad="33", nacimiento='1989-04-08')
    miembro1.save()

    miembro2= familia_nava(nombre="Emma", parentesco="Hija", edad="4", nacimiento='2018-06-03')
    miembro2.save()

    miembro3= familia_nava(nombre="Silvia", parentesco="Madre", edad="52", nacimiento='1969-09-24')
    miembro3.save()

    miembro4= familia_nava(nombre="Miguel", parentesco="Padre", edad="53", nacimiento='1968-08-06')
    miembro4.save()

    pariente=f"---------------------------------------------------------<br>Tu familia es:<br>---------------------------------------------------------<br><br> o{miembro1.parentesco}: {miembro1.nombre}, nació el {miembro1.nacimiento} y tiene {miembro1.edad} años<br><br> o{miembro2.parentesco}: {miembro2.nombre}, nació el {miembro2.nacimiento}y tiene {miembro2.edad} años<br><br> o{miembro3.parentesco}: {miembro3.nombre}, nació el {miembro3.nacimiento} y tiene {miembro3.edad} años<br><br> o{miembro4.parentesco}: {miembro4.nombre}, nació el {miembro4.nacimiento} y tiene {miembro4.edad} años<br>"

    return HttpResponse(pariente)

def ubicacion(request):
    return render (request, "family/ubicacion.html")

def inicio(request):
    return render (request, "family/inicio.html")
    
def hobbies(request):
    return render (request, "family/hobbies.html")

def buscar(request):
    respuesta=f"Estoy buscando la persona {request.GET['nombre']}"
    return HttpResponse(respuesta)

def busquedafamilia(request):
    return render(request, "family/busquedafamilia.html")

def hobbieformulario (request):
    
    if request.method == 'POST':
        miformulario= Hobbieformulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            hobbie= hobbies(nombre=informacion['nombre'], horas_sem=informacion['horas_sem'])
            hobbie.save()
            return render(request, "family/inicio.html")
    else:
        miformulario=Hobbieformulario()
    return render(request, "family/hobbierformulario.html",{"miformulario":miformulario})
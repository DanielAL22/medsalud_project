from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Mundo MedSalud</h1>")

def principal(request):
    return render(request=request, template_name= "principal.html", context={})

def paciente(request):
    return render(request=request, template_name= "pages/opciones_pac.html", context={})

def medico(request):
    return render(request=request, template_name= "pages/opciones_med.html", context={})

def administrador(request):
    return render(request=request, template_name= "pages/opciones_adm.html", context={})

# def principal(request):
#     return render(request=request, template_name= "principal.html", context={})

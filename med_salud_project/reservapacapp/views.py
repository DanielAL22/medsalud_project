from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola_paciente(request):
    return HttpResponse("<h1>Hola Mundo desde reserva paciente</h1>")


def principal_pac(request):
    return render(request=request, template_name= "pages/opciones_res.html", context={})


def buscar_reserva(request):
    resultados_busqueda = [
    {"fecha": "2024-04-16", "hora": "10:00", "medico": "Dr. Perez", "planta": "3", "box": "B1"},
    {"fecha": "2024-04-17", "hora": "11:30", "medico": "Dra. Garcia", "planta": "2", "box": "A3"},
    {"fecha": "2024-04-18", "hora": "09:45", "medico": "Dr. Rodriguez", "planta": "1", "box": "C2"},
    {"fecha": "2024-04-19", "hora": "14:15", "medico": "Dra. Martinez", "planta": "4", "box": "A2"},
    {"fecha": "2024-04-20", "hora": "08:30", "medico": "Dr. Lopez", "planta": "2", "box": "B3"}
]
    
    
    dic_buscar_reserva = {
        "resultados_busqueda": resultados_busqueda
    }
    
    return render(request=request, template_name= "pages/buscar_anular_res.html", context=dic_buscar_reserva)
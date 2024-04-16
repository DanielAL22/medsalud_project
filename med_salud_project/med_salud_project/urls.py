"""
URL configuration for med_salud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principalapp.views import hola, principal, paciente, medico, administrador
from reservapacapp.views import hola_paciente, principal_pac, buscar_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', hola),
    path('medsalud/', principal, name='principal'),
    path('paciente/', paciente, name='paciente'),
    path('medico/', medico, name='medico'),
    path('administrador/', administrador, name='administrador'),
    path('paciente/hola_mundo/', hola_paciente),
    path('paciente/reserva/', principal_pac),
    path('paciente/reserva/buscar/', buscar_reserva),
]

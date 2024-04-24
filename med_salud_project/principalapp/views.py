from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from principalapp.forms import CustomUserCreationForm

# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Mundo MedSalud</h1>")



def inicio(request):
    return render(request=request, template_name= "pages/inicio.html", context={})


@login_required
def area_privada(request):
    # return render(request=request, template_name= "pages/opciones_pac.html", context={})
    if request.user.groups.filter(name='pacientes').exists():
        return render(request, 'pages/opciones_pac.html', {})
    
    elif request.user.groups.filter(name='medicos').exists():
        return render(request, 'pages/opciones_med.html', {})
        
    elif request.user.groups.filter(name='administradores').exists():
        return render(request, 'pages/opciones_adm.html', {})
    
    else:
        HttpResponseRedirect('/admin')
        
    



# @login_required
# def medico(request):
#     return render(request=request, template_name= "pages/opciones_med.html", context={})


# @login_required
# def administrador(request):
#     return render(request=request, template_name= "pages/opciones_adm.html", context={})


def salir(request):
    logout(request)
    return render(request=request, template_name="registration/logout.html", context={})
    # return redirect("/")
    
    
def registro(request):
    # data = {"form": CustomUserCreationForm()}
    
    if request.method == "POST":
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            #logeo automático al registrarse
            #authenticate devuelve un objeto User si las credenciales son correctas
            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            #hacemos el login
            login(request, user)
            
            return HttpResponseRedirect('/opciones')
        
    else:
        # Crea una instancia vacía del formulario ContactFormForm si la solicitud no es de tipo POST, osea si es GET (solicitud)
        user_creation_form = CustomUserCreationForm()
    
    return render(request=request, template_name="registration/register.html", context={'form': user_creation_form})



#en este archivo se va a ejecutar la operacion por la cual cuando se recibe la grabacion de un usuario este se asinga a un grupo automaticamente

#importamos el modelo de grupos para poder grabar en el el grupo que definamos
from django.contrib.auth.models import Group
#un reciver es una herramienta para manejar signals, son eventos que se emiten en un aapp cuando se da una accion (como guardar los datos de un nuevo usuario)
from django.dispatch import receiver
#aqui tambien importamos el post_save
from django.db.models.signals import post_save

from .models import Profile

@receiver(post_save, sender=Profile)
#definimos la funcion de agregar un usuario a un grupo
def add_user_to_pacientes_group(sender, instance, created, **kwargs):
    if created:
        try:
            pacientes = Group.objects.get(name="pacientes")

#https://www.youtube.com/watch?v=p17T7uZKgFg
#20:57
from django.db import models
from django.contrib.auth.models import User  #traemos la tabla user que crea django por defecto
from django.db.models.signals import post_save

# Create your models here.

#PERFIL DE USUARIO
class Profile(models.Model):
    #relacion uno a uno
    #definimos el borrado en cascada en caso de que el usuario se elimine
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name = 'Imagen de perfil')
    adress = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección') #al crear un usuario la direccion estara en blanco
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = [-id] #indica el orden, arriba del todo va a estar el registro más reciente que fue creado
        
        
    def __str__(self) -> str:
        return self.user.username
    
    

#al momento de crear el usuario se tiene que crear el perfil, eso se hace con dos funciones

def create_user_profile(sender, instance, created, **kwargs):
    """
    Hace que cuando creo un usuario se crea el perfil
    """
    if created:
        Profile.objects.create(user=instance)


#hace que cuando se crea el perfil, termina impactando en la base de datos de perfiles
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
#para que esto funcione tengo que hacer un post save
#con esto logro conectar el usuario con el perfil
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
    

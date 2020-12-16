"""importamos los modelos que van relacionados con esta aplicacion"""
from django.db import models
from users.models import User
from tags.models import Tag

"""creamos nuestro modelo de clases"""
class Newsletter(models.Model):
    """ponemos los campos"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    """Declaro las dos opciones disponibles para el tipo de dato ImageField, para poder saber el alto y ancho de la imagen que suben"""
    image = models.ImageField(upload_to='assets/newsletters')
    meta = models.CharField(max_length=30)
    frequency = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)

    """hacemos la relacion de users y tags"""
    users = models.ManyToManyField(User, related_name='users')
    tags = models.ManyToManyField(Tag, related_name='tags')

    """hacemos visible el campo nombre para este modelo"""
    def __str__(self):
        return self.name
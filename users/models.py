#importamos la libreria
from django.db import models

#creamos una clase para generar nuestro modelo para la aplicacion
class User(models.Model):
    #generamos los campos para dicho modelo
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

#mostramos el nombre de los campos del modelo para que sea visible en las vistas
    def __str__(self):
        return self.name
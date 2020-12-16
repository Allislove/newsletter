#importamos la libreria
from django.db import models

#generamos el modelos con una clase
class Tag(models.Model):
    #generamos los campos del modelo
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

#mostramos el nombre del modelo en la vista
    def __str__(self):
        return self.name

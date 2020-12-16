#importamos las librerias y modelos necesarios
from django.db import models
from users.models import User
from newsletters.models import Newsletter
from datetime import datetime

#creamos una clase para generar el modelo
class Vote(models.Model):
    #generamos los campos necesarios para este modelo
    updatedAt = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    

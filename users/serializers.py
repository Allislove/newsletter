#impotamos la libreria  para generar los serializadores y el modelo de user
from users.models import User
from rest_framework import serializers

#creamos una clase para generar los serializer
class UserSerializer(serializers.ModelSerializer):
    #creamos un meta para mostrar los campos del modelo
    class Meta:
        model = User
        fields = ('id','name', 'lastName', 'email')
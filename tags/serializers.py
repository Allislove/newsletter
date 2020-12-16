#importamos la libreria y el modelo
from tags.models import Tag
from rest_framework import serializers

#generamos los serializadores
class TagSerializer(serializers.ModelSerializer):
    #creamos un meta para traer todos los campos del modelo
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')



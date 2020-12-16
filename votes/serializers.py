#imprortamos el modelo y la libreria
from votes.models import Vote
from rest_framework import serializers

#creamos una clase para generar los serializadores
class VoteSerializer(serializers.ModelSerializer):
    #creamos un meta para traer todos los campos del modelo
    class Meta:
        model = Vote
        fields = '__all__'
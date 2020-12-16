
"""importo la libreria y el modelo"""
from newsletters.models import Newsletter
from rest_framework import serializers

"""genero mi serializador a traves de una clase"""
class NewsletterSerializer(serializers.ModelSerializer):
    """genero una meta para llamar el nombre del modelo"""
    class Meta:
        model = Newsletter
        """traigo todos los campos de mi modelo"""
        fields = '__all__'
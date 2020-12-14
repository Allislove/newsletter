from usuarios.models import Usuario
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('name', 'lastName', 'email')
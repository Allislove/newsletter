#importamos la libreria y los serializadores y el modelo
from votes.serializers import VoteSerializer
from votes.models import Vote
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from tags.serializers import TagSerializer
from tags.models import Tag
from users.models import User, User, User
from users.serializers import UserSerializer


#creamos una clase para generar las vistas
class VotesViewSet(viewsets.ModelViewSet):
    # 5. Como usuario quiero poder votar por un boletín para que se haga el lanzamiento de este boletín.
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
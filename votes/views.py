from votes.serializers import VoteSerializer
from votes.models import Vote
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from tags.serializers import TagSerializer
from tags.models import Tag
from users.models import User, User, User
from users.serializers import UserSerializer

# 5. Como usuario quiero poder votar por un boletín para que se haga el lanzamiento de este boletín.

class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
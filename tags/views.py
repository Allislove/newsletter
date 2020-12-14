from tags.serializers import TagSerializer
from tags.models import Tag
from rest_framework import viewsets
from rest_framework.response import Response

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



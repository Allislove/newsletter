from newsletters.serializers import NewsletterSerializer
from newsletters.models import Newsletter
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from tags.serializers import TagSerializer
from tags.models import Tag
from users.models import User, User, User
from users.serializers import UserSerializer

#2. Poder ver la listas de boletines creados y ver su categoria#

class NewsViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, request, pk=None):
        newsletter = self.get_object()
        if request.method== 'GET':
            serialized = TagSerializer(newsletter.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method== 'POST':
            newsletter_id = request.data['tags']
            for tag_id in newsletter_id:
                tag = Tag.objects.get(id=int(tag_id))
                newsletter.tags.add(tag)
            return Response(status = status.HTTP_201_CREATED)
        if request.method== 'DELETE':
            newsletter_id = request.data['tags']
            for tag_id in newsletter_id:
                tag = Tag.objects.get(id=int(tag_id))
                newsletter.tags.remove(tag)
            return Response(status = status.HTTP_204_NO_CONTENT)
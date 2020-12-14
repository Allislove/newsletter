from django.shortcuts import render
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from users.models import User
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def newsletters(self, request, pk=None):
        user = self.get_object()
    # 6. Como usuario quiero iniciar sesión para poder ver los boletines a los que estoy suscrito.
        if request.method== 'GET':
            id = Newsletter.objects.filter(users=int(user.id))
            serialized = NewsletterSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)



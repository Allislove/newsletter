from newsletters.serializers import NewsletterSerializer
from newsletters.models import Newsletter
from rest_framework import viewsets
from rest_framework.response import Response

class NewsViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

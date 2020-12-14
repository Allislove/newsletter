from newsletters.models import Newsletter
from rest_framework import serializers

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'image', 'meta')


        
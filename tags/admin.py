"""iimportamos la libreria y el modelo de la aplicacion"""
from django.contrib import admin
from tags.models import Tag
"""registramos la urls"""
admin.site.register(Tag)

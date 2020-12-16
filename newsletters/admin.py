"""importamos modelos"""
from django.contrib import admin
from newsletters.models import Newsletter
"""registramos la urls de la aplicacion"""
admin.site.register(Newsletter)


from django.db import models
from users.models import User
from newsletters.models import Newsletter
from datetime import datetime

class Vote(models.Model):
    
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    

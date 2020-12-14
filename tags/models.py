from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings


class DigitalArtWork(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField()
    image_alt = models.CharField(max_length=254)
    description = models.TextField()
    carousel = models.BooleanField()

    def __str__(self):
        return self.name

""" Models for Digital Art Works """
from django.db import models


class DigitalArtWork(models.Model):
    """ Digital Art Works Model """
    name = models.CharField(max_length=254)
    image = models.ImageField()
    image_alt = models.CharField(max_length=254)
    description = models.TextField()
    carousel = models.BooleanField()

    def __str__(self):
        return str(self.name)

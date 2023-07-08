import os

from django.db import models
from django.conf import settings


class DigitalArtWork(models.Model):
    name = models.CharField(max_length=254)
    daw_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()
    image_alt = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=254, null=True, blank=True)
    file_type = models.CharField(max_length=10, null=True, blank=True)
    carousel = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        image_url = os.path.join(settings.MEDIA_ROOT, self.image.url)
        return image_url

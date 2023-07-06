from django.db import models

# Create your models here.


class DigitalArtWork(models.Model):
    name = models.CharField(max_length=254)
    daw_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=254, null=True, blank=True)
    file_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models

from digital_artworks.models import DigitalArtWork


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=245)
    friendly_name = models.CharField(max_length=245, null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Subcategories'
    name = models.CharField(max_length=245)
    friendly_name = models.CharField(max_length=245, null=True, blank=True)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=True,
                                blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL)
    digital_artwork = models.ForeignKey('digital_artworks.DigitalArtWork',
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL,
                                        related_name='products')

    def __str__(self):
        return self.name

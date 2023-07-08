from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=245)
    friendly_name = models.CharField(max_length=245, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    name = models.CharField(max_length=245)
    friendly_name = models.CharField(max_length=245, null=True, blank=True)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=True,
                                blank=True)
    description = models.TextField()
    image_url = models.ImageField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

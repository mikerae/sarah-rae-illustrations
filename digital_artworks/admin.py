from django.contrib import admin
from .models import DigitalArtWork


class DigitalArtWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_alt',
        'description',
    )


admin.site.register(DigitalArtWork, DigitalArtWorkAdmin)

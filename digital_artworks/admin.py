from django.contrib import admin
from .models import DigitalArtWork


class DigitalArtWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_alt',
        'description',
        'size',
        'file_type',
    )


admin.site.register(DigitalArtWork, DigitalArtWorkAdmin)

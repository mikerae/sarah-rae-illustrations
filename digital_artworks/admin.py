from django.contrib import admin
from .models import DigitalArtWork

# Register your models here.


class DigitalArtWorkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'size',
        'file_type',
        'daw_url',
    )


admin.site.register(DigitalArtWork, DigitalArtWorkAdmin)

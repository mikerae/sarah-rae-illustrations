""" Admin settings for UserProfile Models"""
from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ Display for UserProfile """
    list_display = (
        'user',
        'default_phone_number',
        'default_postcode',
        'default_street_address_1',
        'default_street_address_2',
        'default_county',
        'default_country',
        'default_town_or_city',
    )


admin.site.register(UserProfile, UserProfileAdmin)

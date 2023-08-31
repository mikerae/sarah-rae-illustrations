""" App Config for cart app """
from django.apps import AppConfig


class CartConfig(AppConfig):
    """ config class for cart app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'

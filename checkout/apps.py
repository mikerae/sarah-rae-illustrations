""" Config for checjout app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Config for checkout app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

# Copied from Code Institute Boutique Ado walkthrough
    def ready(self):
        import checkout.signals
# End copy

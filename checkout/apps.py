from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

# Copied from Code Institute Boutique Ado walkthrough
    def ready(self):
        import checkout.signals
# End copy

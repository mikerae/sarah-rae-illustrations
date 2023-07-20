""" Provides Project level signals when a save or delete action occurs """
# Copied from Code Institute Boutique Ado walkthrough
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
        Update order total on lineitem update/create
    """
    print('on save: signal received')  # Test post-save signal
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
        Update order total on lineitem delete
    """
    print('on delete: signal received')  # Test post-delete signal
    instance.order.update_total()

# End Copy

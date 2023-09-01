""" Tools for use in cart app  """
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate and return line order subtotal """
    return price * quantity

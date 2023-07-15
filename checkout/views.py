from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    print('Checkout called')
    if not cart:
        message.error(request, "Your Shopping Cart is empty")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NUDuCLQavTTy4OO03tEmLca6UilHp4doQh2Oaqz0QO5sPkeJQB6cEBsVLYxXyW9ld8IwV0bQAXG6kKBAF0WWYaS00iaYW3E6Q',  # noqa E501
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

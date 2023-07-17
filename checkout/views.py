import json
import os
import stripe

from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

from .forms import OrderForm
from cart.contexts import cart_contents

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        message.error(request, "Your Shopping Cart is empty")
        return redirect(reverse('shop'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            automatic_payment_methods={
                'enabled': True,
            },
        )
    except Exception as e:
        messages.warning(request, f'Oh dear! There was an error: ${e}')
        return redirect(reverse('cart'))

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

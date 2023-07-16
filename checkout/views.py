import json
import os
import stripe

from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

from .forms import OrderForm

stripe_public_key = settings.STRIPE_PUBLIC_KEY


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        message.error(request, "Your Shopping Cart is empty")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': 'test client secret',
    }

    return render(request, template, context)


# def calculate_order_amount(items):
#     # Replace this constant with a calculation of the order's amount
#     # Calculate the order total on the server to prevent
#     # people from directly manipulating the amount on the client
#     return 1400


# def create_payment_intent(request, method="POST", *args, **kwargs):
#     try:
#         data = json.loads(request.data)
#         # Create a PaymentIntent with the order amount and currency
#         intent = stripe.PaymentIntent.create(
#             amount=calculate_order_amount(data['items']),
#             currency='gbp',
#             automatic_payment_methods={
#                 'enabled': True,
#             },
#         )
#         return jsonify({
#             'clientSecret': intent['client_secret']
#         })
#     except Exception as e:
#         return jsonify(error=str(e)), 403

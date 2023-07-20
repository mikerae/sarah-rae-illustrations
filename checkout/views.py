""" Module to handle Checkout calls """
import json

import stripe

from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404,
                              HttpResponse)
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from shop.models import Product
from cart.contexts import cart_contents
from .forms import OrderForm
from .models import OrderLineItem


stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


@require_POST
def save_userdata_checked(request):
    """
    Recieves boolean indicating if the user
    wants to save their user details for future user
    in this site. (Stripe has already asked this for
    stripe data). If so , 'True' is returned for storage and
    futher processing.
    """
    print('save_userdata_checked is called')
    try:
        save_info = request.POST.get('save-info')
        request.session['save-info'] = save_info
        django_save_info = request.session['save-info']
        print(f'save-info stored in current session is: {django_save_info}')
        return HttpResponse(status=200)
    except Exception as e:
        print(f'save-info was not in the current session. {e}')
        return HttpResponse(content=e, status=400) 


def checkout(request):
    """ Handles Checkout calls """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing. \
            Did you forget to set it in your environment?')

    checkout_success_url = request.build_absolute_uri('checkout_success/')

    template = 'checkout/checkout.html'
    context = {
        # order_form = OrderForm()
        'stripe_public_key': stripe_public_key,
        'checkout_success_url': checkout_success_url,
    }

    return render(request, template, context)


def checkout_success(request):
    """
    Create Order after sucessful payment.
    """
    stripe_pid = request.GET['payment_intent']

    stripe.api_key = stripe_secret_key
    payment_intent = stripe.PaymentIntent.retrieve(stripe_pid)

    cart = request.session.get('cart', {})
    save_info = request.session['save-info']
    print(f'checkout-success retrieved \
        save-info from the curent \
            session as: {save_info}')

    form_data = {
        'full_name': payment_intent['shipping']['name'],
        'email': payment_intent['receipt_email'],
        'phone_nubmer': payment_intent['shipping']['phone'],
        'country': payment_intent['shipping']['address']['country'],
        'town_or_city': payment_intent['shipping']['address']['city'],
        'street_address_1': payment_intent['shipping']['address']['line1'],
        'street_address_2': payment_intent['shipping']['address']['line2'],
        'postcode': payment_intent['shipping']['address']['postal_code'],
        'county': payment_intent['shipping']['address']['state'],
    }

    order_form = OrderForm(form_data)

    if order_form.is_valid():
        print('Order is valid')
        order = order_form.save(commit=False)
        order.stripe_pid = stripe_pid
        order.original_cart = json.dumps(cart)
        order.save()

        for item_id, item_data in cart.items():

            product = get_object_or_404(Product, pk=item_id)
            if isinstance(item_data, int):
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_line_item.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order.order_number}. A confirmation email \
            will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def order_form_not_valid(request):
    """ Handles Invalid Addresss Payment Data for Orders """
    messages.error(request, 'There was an error with your form. \
        Please double check your information.')

    # if order_form.is_valid():
    template = 'order_form_not_valid.html'

    return render(request, template)


def create_payment_intent(request):
    """
    Creates a stripe paymentIntent  and passes it
    to stripe Payment Element
    """

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Shopping Cart is empty")
        return redirect(reverse('shop'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    try:
        # Create a Payment Intent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        messages.warning(request, f'Oh dear! There was an error: ${e}')
        return JsonResponse(error=str(e), data=403)
    return

""" Module to handle Checkout calls """
import os
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
from .models import Order, OrderLineItem


stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


# @require_POST
# def cache_checkout_data(request):
#     """ Caches checkout data for processing """
#     try:
#         stripe_pid = request.POST.get('client_secret').split('_secret'[0])
#         print(stripe_pid)  # test stripe_pid
#         stripe.PaymentIntent.modify(stripe_pid, matadata={
#             'cart': json.dumps(request.session.get('cart', {})),
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#             })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, f'Woops! {e} Your payment has not been \
#              processed. Please try again later.')
#     return HttpResponse(contents=3, status=400)


def checkout(request):
    """ Handles Checkout calls """

    cart = request.session.get('cart', {})

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
    # remove *args, **kwargs?

    """
    Handle sucessful checkouts.
    """
    stripe_pid = request.GET['payment_intent']
    client_secret = request.GET['payment_intent_client_secret']

    stripe.api_key = stripe_secret_key
    payment_intent = stripe.PaymentIntent.retrieve(stripe_pid)

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
    print(f'Unsaved Order Form data is: {order_form}')
    if order_form.is_valid():
        print('Order is valid')
        # order = order_form.save(commit=False)
        # order.stripe_pid = stripe_pid
        # order.original_bag = json.dumps(cart)
            # order.save()

    #     for item_id, item_data in cart.items():
    #         try:
    #             product = Product.objects.get(id=item_id)
    #             if isinstance(item_data, int):
    #                 order_line_item = OrderLineItem(
    #                     order=order,
    #                     product=product,
    #                     quantity=item_data,
    #                 )
    #                 order_line_item.save()
    #         except Product.DoesNotExist:
    #             messages.error(request, (
    #                 "One of the products in your \
    #                     bag wasn't found in our database."
    #                 "Please call us for assistance")
    #             )
    #             order.delete()
    #             return redirect(reverse('view_cart'))
    #     request.session['save_info'] = 'save-info' in request.POST
    #     return redirect(
    #                     reverse('checkout_success',
    #                             args=[order.order_number])
    # )

    # if request.user.is_authenticated:
    # try:
    #     profile = UserProfile.objects.get(user=request.user)
    #     order_form = OrderForm(initial={
    #         'full_name': profile.user.get_full_name(),
    #         'email': profile.user.email,
    #         'phone_number': profile.default_phone_number,
    #         'country': profile.default_country,
    #         'postcode': profile.default_postcode,
    #         'town_or_city': profile.default_town_or_city,
    #         'street_address1': profile.default_street_address1,
    #         'street_address2': profile.default_street_address2,
    #         'county': profile.default_county,
    #     })
    # except UserProfile.DoesNotExist:
    #     order_form = OrderForm()
    #     order_form = OrderForm()
    # else:
    #     order_form = OrderForm()
    # save_info = request.session.get('save_info')
    # order = get_object_or_404(Order, order_number=order_number)
    # messages.success(request, f'Order successfully processed! \
    #     Your order number is {order_number}. A confirmation email \
    #         will be sent to {order.email}.')

    # if 'cart' in request.session:
    #     del request.session['cart']
    else:
        print('The order form is not valid')
        order_form_not_valid
        template = 'checkout/order_form_not_valid.html'
        return render(request, template)

    template = 'checkout/checkout_success.html'
    context = {
        # 'order': order,
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

import stripe

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem
from shop.models import Product
from cart.contexts import cart_contents

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


def checkout(request):

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        # form_data = {
        #     'full_name': request.POST['full_name'],
        #     'email': request.POST['email'],
        #     'phone_nubmer': request.POST['phone_nubmer'],
        #     'country': request.POST['country'],
        #     'town_or_city': request.POST['town_or_city'],
        #     'street_address_1': request.POST['street_address_1'],
        #     'street_address_2': request.POST['street_address_2'],
        #     'county': request.POST['county']
        # }
        # print(form_data)

        # order_form = OrderForm(form_data)
        # if order_form.is_valid():
        #     order = order_form.save()
        #     for item_id, item_data in cart.items():
        #         try:
        #             product = Product.objects.get(id=item_id)
        #             if isinstance(item_dat, int):
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
        #                     )
        # else:
        #     messages.error(request, 'There was an error with your form. \
        #         Please double check your information.')
    else:
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
    checkout_success_url = request.build_absolute_uri('/checkout_success/')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'checkout_success_url': checkout_success_url,
    }

    return render(request, template, context)


def checkout_success(request, ordder_number):
    """
    Handle sucessful checkouts.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation email \
            will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, contect)

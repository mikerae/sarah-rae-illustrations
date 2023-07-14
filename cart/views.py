from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from shop.models import Product


def cart(request):
    """ Return render of cart page view.
    """
    site_area = request.path

    context = {
        'site_area': site_area,
    }
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of the desired product to the shopping cart.
    Sessions are used to store cart data during a site user's visit.
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    messages.success(request,
                     f'Added {product.name} to your shopping cart!')
    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust a quantity of the desired product to the shopping cart.
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """
    Remove selected product from the shopping cart.
    """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

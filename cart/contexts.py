"""
    This is the source file for a custom context processor,
    which provides site-level access to various data.
    It is made visible to Django by including 'cart.contexts.cart_contents'
    in the 'context_processors' list in the project settings.
"""

from django.shortcuts import get_object_or_404

from shop.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context

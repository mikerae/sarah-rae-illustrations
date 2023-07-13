"""
    This is the source file for a custom context processor, 
    which provides site-level access to various data.
    It is made visible to Django by including 'cart.contexts.cart_contents'
    in the 'context_processors' list in the project settings.
"""


def cart_contents(requests):

    cart_items = []
    total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context

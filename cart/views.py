from django.shortcuts import render


def cart(request):
    """ Return render of cart page view.
    """
    site_area = request.path

    context = {
        'site_area': site_area,
    }
    return render(request, 'cart/cart.html')

from django.shortcuts import render
from .models import Product


def shop(request):
    """ Render shop landing  page view with shop path as context.
        Show all products, including sorting and searching.
    """
    site_area = request.path
    products = Product.objects.all()

    context = {
        'site_area': site_area,
        'products': products,
    }

    return render(request, 'shop/shop.html', context)

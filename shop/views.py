from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    Render product detail  page view with shop path as context.
    Show product detail for selected product.
    """
    site_area = request.path
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'site_area': site_area,
        'product': product,
    }

    return render(request, 'shop/shop.html', context)

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def shop(request):
    """ Render shop landing  page view with shop path as context.
        Show all products, including sorting and searching.
    """
    site_area = request.path
    products = Product.objects.all()
    query = None
    category = None

    if request.GET:

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            print(products)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "Please enter something to search for"
                    )
                return redirect(reverse('shop'))

            queries = Q(
                name__icontains=query
                ) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'site_area': site_area,
        'products': products,
        'search_term': query,
        'current_category': category,
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

    return render(request, 'shop/product_detail.html', context)

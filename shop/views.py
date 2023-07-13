from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, SubCategory


def shop(request):
    """ Render shop landing  page view with shop path as context.
        Show all products, including sorting and searching.
    """
    site_area = request.path
    products = Product.objects.all()
    query = None
    category = None
    subcategory = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = get_object_or_404(Category, name=category)
            print(f'Catergory: {category}')

        if 'subcategory' in request.GET:
            subcategory = request.GET['subcategory']
            products = products.filter(subcategory__name=subcategory)
            subcategory = get_object_or_404(SubCategory, name=subcategory)
            category = subcategory.category

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'site_area': site_area,
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_subcategory': subcategory,
        'current_sorting': current_sorting
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

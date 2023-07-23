""" Views for the Shop """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category, SubCategory
from .forms import ProductForm


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


@login_required
def add_product(request):
    """ Add a product to the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    if request.method == 'POST':
        print('add_product called')
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            print('there was an error adding your product')
            messages.error(request, 'Failed to add product.Please ensure \
                 the form is valid.')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a shop product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You product has been updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure your form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}.')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('shop'))

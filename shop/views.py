from django.shortcuts import render


def shop(request):
    """ Render shop landing  page view with shop path as context.
    """
    site_area = request.path
    context = {
        'site_area': site_area,
    }

    return render(request, 'shop/shop.html', context)

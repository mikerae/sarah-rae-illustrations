from django.shortcuts import render


def shop(request):
    """ Return shop landing  page view.
    """

    return render(request, 'shop/shop.html')

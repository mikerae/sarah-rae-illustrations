from django.shortcuts import render


def digital_artworks(request):
    """ Return commissions landing  page view.
    """

    return render(request, 'digital_artworks/digital_artworks.html')

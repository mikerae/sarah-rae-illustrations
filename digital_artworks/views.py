from django.shortcuts import render, get_object_or_404
from .models import DigitalArtWork


def digital_artworks(request):
    """ Render Digital Artworks landing  page view with gallery path as
        context.
        Show all Digital Artworks, including sorting and searching.
    """
    site_area = request.path
    digital_artworks = DigitalArtWork.objects.all()

    context = {
        'site_area': site_area,
        'digital_artworks': digital_artworks,
    }

    return render(request, 'digital_artworks/digital_artworks.html', context)


def digital_artwork_detail(request, digital_artwork_id):
    """
    Render digital artwork detail  page view with gallery path as context.
    Show product digital artwork for selected product.
    """
    site_area = request.path
    digital_artwork = get_object_or_404(DigitalArtWork, pk=digital_artwork_id)

    context = {
        'site_area': site_area,
        'digital_artwork': digital_artwork,
    }

    return render(request,
                  'digital_artworks/digital_artwork_detail.html', context)

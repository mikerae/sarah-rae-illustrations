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

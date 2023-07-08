from django.shortcuts import render


def digital_artworks(request):
    """ Render Digital Art works landing  page view with digital art works
    path as context.
    """
    site_area = request.path
    context = {
        'site_area': site_area,
    }

    return render(request, 'digital_artworks/digital_artworks.html', context)

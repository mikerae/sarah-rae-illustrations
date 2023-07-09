from django.shortcuts import render
from digital_artworks.models import DigitalArtWork

# Create your views here.


def index(request):
    """ Return index page view and Digital Art Work context
        data for Carousel.
    """
    artworks = DigitalArtWork.objects.all()
    carousel_artworks = artworks.filter(carousel=True)
    context = {
        'carousel_artworks': carousel_artworks,
    }
    print(context)
    return render(request, 'home/index.html', context)

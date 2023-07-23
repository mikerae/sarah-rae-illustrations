""" Views for the Gallery """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import DigitalArtWork
from .forms import DigitalArtWorkForm


def digitalartworks(request):
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
    Show artwork digital artwork for selected artwork.
    """
    site_area = request.path
    digital_artwork = get_object_or_404(DigitalArtWork, pk=digital_artwork_id)

    context = {
        'site_area': site_area,
        'digital_artwork': digital_artwork,
    }

    return render(request,
                  'digital_artworks/digital_artwork_detail.html', context)


@login_required
def add_digital_artwork(request):
    """ Add a artwork to the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    if request.method == 'POST':
        print('add_digital_artwork called')
        form = DigitalArtWorkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            messages.success(request, 'Successfully added artwork!')
            return redirect(reverse('digital_artwork_detail', args=[artwork.id]))
        else:
            print('there was an error adding your artwork')
            messages.error(request, 'Failed to add artwork. Please ensure \
                 the form is valid.')
    else:
        form = DigitalArtWorkForm()

    template = 'digital_artworks/add_digitalartwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_digital_artwork(request, digital_artwork_id):
    """ Edit a gallery artwork """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    artwork = get_object_or_404(DigitalArtWork, pk=digital_artwork_id)
    if request.method == "POST":
        form = DigitalArtWorkForm(request.POST,
                                  request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'You artwork has been updated.')
            return redirect(reverse('digital_artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, 'Failed to update artwork. \
                Please ensure your form is valid')
    else:
        form = DigitalArtWorkForm(instance=artwork)
        messages.info(request, f'You are editing {artwork.name}.')

    template = 'digital_artworks/edit_digitalartwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


@login_required
def delete_digital_artwork(request, digital_artwork_id):
    """ Delete a artwork from the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do this!')
        return redirect(reverse, 'home')
    artwork = get_object_or_404(DigitalArtWork, pk=digital_artwork_id)
    artwork.delete()
    messages.success(request, 'DigitalArtWork deleted')
    return redirect(reverse('digital_artworks'))

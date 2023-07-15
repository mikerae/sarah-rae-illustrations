from django.shortcuts import render


def commissions(request):
    """ Return commissions landing  page view.
    """
    site_area = request.path

    context = {
        'site_area': site_area,
    }
    return render(request, 'commissions/commissions.html', context)

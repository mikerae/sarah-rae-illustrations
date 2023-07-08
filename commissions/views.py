from django.shortcuts import render


def commissions(request):
    """ Return commissions landing  page view.
    """

    return render(request, 'commissions/commissions.html')

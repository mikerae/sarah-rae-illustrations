""" Veiws for about_sarah app """
from django.shortcuts import render


def about_sarah(request):
    """ Return about_sarah landing  page view.
    """
    site_area = request.path

    context = {
        'site_area': site_area,
    }

    return render(request, 'about_sarah/about_sarah.html', context)

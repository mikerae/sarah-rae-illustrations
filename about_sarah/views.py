from django.shortcuts import render


def about_sarah(request):
    """ Return about_sarah landing  page view.
    """

    return render(request, 'about_sarah/about_sarah.html')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_artworks, name='digital_artworks'),
    path('<digital_artwork_id>',
         views.digital_artwork_detail, name='digital_artwork_detail')
]

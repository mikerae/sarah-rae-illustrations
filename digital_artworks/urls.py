""" Urls for digital_artworks app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.digitalartworks, name='digital_artworks'),
    path('<digital_artwork_id>', views.digital_artwork_detail,
         name='digital_artwork_detail'),
    path('add/', views.add_digital_artwork, name='add_digital_artwork'),
    path('edit/<int:digital_artwork_id>', views.edit_digital_artwork,
         name='edit_digital_artwork'),
    path('delete/<int:digital_artwork_id>',
         views.delete_digital_artwork, name='delete_digital_artwork')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_artworks, name='digital_artworks')
]

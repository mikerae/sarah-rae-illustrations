""" Form for DigitalArtWork admin """
from django import forms
from .widgets import CustomClearableFileInput
from .models import DigitalArtWork


class DigitalArtWorkForm(forms.ModelForm):
    """ A form to manage the shop digital artworks """

    class Meta:
        """ Custom fields """
        model = DigitalArtWork
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

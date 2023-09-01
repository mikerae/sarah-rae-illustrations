""" Forms for profile app """
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Checkout Order Form holding User Profile shipping data """
    class Meta:
        """ Meta Data for UserProfile form"""
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Post Code',
            'default_town_or_city': 'Town or City',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-sri rounded-0 profile-form-input'  # noqa E501
            self.fields[field].label = False

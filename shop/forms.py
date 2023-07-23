""" Form for Product admin """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, SubCategory


class ProductForm(forms.ModelForm):
    """ A form to manage the shop products """

    class Meta:
        """ Custom fields """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-sri rounded-0'

        subcategories = SubCategory.objects.all()
        subcategory_friendly_names = [(
            sc.id, sc.get_friendly_name()
            ) for sc in subcategories]
        self.fields['subcategory'].choices = subcategory_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-sri text-sri-logo rounded-0'

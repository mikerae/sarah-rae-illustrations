from django import forms
from .models import Product, Category, SubCategory


classs ProductForm(forms.ModelForm):

    class Meta:
        model = Productfirelds = '__all__'

    def __init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [(
            c.id, c.get_friendly_name()
            ) for c in categories]
        subcategories = SubCategory.objects.all()
        subcategory_friendly_names = [(
            sc.id, sc.get_friendly_name()
            ) for sc in subcategories]

        self.fields['category'].choices = category_friendly_names
        self.fields['subcategory'].choices = subcategory_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs[['class']] = 'border-sri rounded-0'



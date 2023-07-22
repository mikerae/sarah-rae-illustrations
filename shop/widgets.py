""" Custom widget to style Forms with Image Fields """
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ Custom params """
    clear_checkbox_lable = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'shop/custom_widget_templates/custom_clearable_file_input.html'  # noqa E501

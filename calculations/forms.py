from django import forms
from materials.models import Product
from .models import Assembly
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class CalculateForm(forms.Form):
    surface = forms.IntegerField(required=False, label="Powierzchnia:", widget=forms.NumberInput(attrs={'placeholder': u'm²'}))
    wood = forms.ModelChoiceField(label="Rodzaj drewna", queryset=Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name'))
    where_to = forms.ModelChoiceField(queryset=Assembly.objects.order_by('price_m2'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-md-6 mb-3 text-center'
        self.helper.layout = Layout(
            Row(
                Column('surface', css_class='form-group col-md-6 mb-0'),
                Column('surface.label', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )
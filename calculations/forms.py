from django import forms
from django.forms.widgets import HiddenInput

from django.core.validators import RegexValidator

from materials.models import Product
from .models import Assembly



class CalculateForm(forms.Form):
    surface = forms.IntegerField(required=True, label=False,widget=forms.NumberInput(attrs={'placeholder': u'm²'}))
    wood = forms.ModelChoiceField(required=True, label=False, queryset=Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name'))
    where_to = forms.ModelChoiceField(required=True, label=False,queryset=Assembly.objects.order_by('price_m2'))

    surface.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię tarasu w m²')", oninput="setCustomValidity('')")
    wood.widget.attrs.update(oninvalid="setCustomValidity('Wybierz rodzaj drewna.')", oninput="setCustomValidity('')")
    where_to.widget.attrs.update(oninvalid="setCustomValidity('Wybierz typ zabudowy')", oninput="setCustomValidity('')")

class InquiryModalForm(CalculateForm):
    name = forms.CharField(label='Imię:', max_length='24', required=True,)
    email = forms.EmailField(label='Email:', required=True)
    phone = forms.CharField(label='Nr. telefonu:', max_length=12, required=True)
    message = forms.CharField(widget=forms.Textarea)


    name.widget.attrs.update(oninvalid="setCustomValidity('Podaj swoje Imię')", oninput="setCustomValidity('')")
    email.widget.attrs.update(oninvalid="setCustomValidity('Podaj adres email')", oninput="setCustomValidity('')")

    def __init__(self, *args, **kwargs):
        super(InquiryModalForm, self).__init__(*args, **kwargs)
        self.fields['surface'].widget = HiddenInput()
        self.fields['wood'].widget = HiddenInput()
        self.fields['where_to'].widget = HiddenInput()

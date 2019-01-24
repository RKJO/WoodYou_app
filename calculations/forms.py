from django import forms
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

class InquiryModalForm(forms.Form):
    name = forms.CharField(label='Imię:', max_length='24', required=True,)
    email = forms.EmailField(label='Email:', required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Numer telefonu musi być podany w formacie: '+48123456789'.")
    phone = forms.CharField(label='Nr. telefonu:',validators=[phone_regex], max_length=12,)
    message = forms.CharField(widget=forms.Textarea)

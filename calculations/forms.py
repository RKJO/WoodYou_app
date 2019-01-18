from django import forms

from materials.models import Product
from .models import Assembly



class CalculateForm(forms.Form):
    surface = forms.IntegerField(required=True, label=False, widget=forms.NumberInput(attrs={'placeholder': u'm²'}))
    wood = forms.ModelChoiceField(required=True, label=False, queryset=Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name'))
    where_to = forms.ModelChoiceField(required=True, label=False,queryset=Assembly.objects.order_by('price_m2'))

    surface.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię tarasu w m²')", oninput="setCustomValidity('')")
    wood.widget.attrs.update(oninvalid="setCustomValidity('Wybierz rodzaj drewna.')", oninput="setCustomValidity('')")
    where_to.widget.attrs.update(oninvalid="setCustomValidity('Wybierz typ zabudowy')", oninput="setCustomValidity('')")

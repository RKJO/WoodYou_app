from django import forms
from django.forms.widgets import HiddenInput

from .models import Ralization



class RealizationSearchForm(forms.Form):

    queryset=Ralization.objects.order_by('-realization_date')

    USED_WOODS = tuple(set((product.used_wood, str(product.used_wood)) for product in queryset))
    
    powierzchnia_od = forms.IntegerField(required=False, label=False,widget=forms.NumberInput(attrs={'placeholder': u'Powierzchnia od:'}))
    powierzchnia_do = forms.IntegerField(required=False, label=False,widget=forms.NumberInput(attrs={'placeholder': u'Powierzchnia do:'}))
    rodzaj_drewna = forms.ChoiceField(choices=(('', 'Rodzaj drewna'),) + USED_WOODS, label=False, required=False)

    # powierzchnia_od.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię zabudowy w m²')", oninput="setCustomValidity('')")
    # powierzchnia_do.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię zabudowy w m²')", oninput="setCustomValidity('')")
    # wood.widget.attrs.update(oninvalid="setCustomValidity('Wybierz rodzaj drewna.')", oninput="setCustomValidity('')")
    # rodzaj_drewna.widget.attrs.update(oninvalid="setCustomValidity('Wybierz typ zabudowy')", oninput="setCustomValidity('')")


from django import forms
from django.forms.widgets import HiddenInput

from .models import Ralization



class RealizationSearchForm(forms.Form):
    
    powierzchnia_od = forms.IntegerField(required=False, label=False,widget=forms.NumberInput(attrs={'placeholder': u'Powierzchnia od:'}))
    powierzchnia_do = forms.IntegerField(required=False, label=False,widget=forms.NumberInput(attrs={'placeholder': u'Powierzchnia do:'}))
    rodzaj_drewna = forms.ModelChoiceField(required=False, label=False, empty_label="Rodzaj drewna",queryset=Ralization.objects.order_by('-realization_date'))

    # powierzchnia_od.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię zabudowy w m²')", oninput="setCustomValidity('')")
    # powierzchnia_do.widget.attrs.update(oninvalid="setCustomValidity('Podaj powierzchnię zabudowy w m²')", oninput="setCustomValidity('')")
    # wood.widget.attrs.update(oninvalid="setCustomValidity('Wybierz rodzaj drewna.')", oninput="setCustomValidity('')")
    # rodzaj_drewna.widget.attrs.update(oninvalid="setCustomValidity('Wybierz typ zabudowy')", oninput="setCustomValidity('')")


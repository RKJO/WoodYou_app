from django.contrib import admin
from django.db import models

from .models import Ralization
from django.forms import CheckboxSelectMultiple


# @admin.register(Ralization)
class RalizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'location', 'realization_date')
    list_display_links = ('name',)
    list_filter = ('used_wood', 'category_name')
    list_editable = ('cost',)
    search_fields = ('name', 'used_wood', 'location')
    list_per_page = 25

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Ralization, RalizationAdmin)
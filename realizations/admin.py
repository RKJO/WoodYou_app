from django.contrib import admin
from .models import Ralization

# @admin.register(Ralization)
class RalizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'location', 'realization_date')
    list_display_links = ('name',)
    list_filter = ('used_wood', 'category_name')
    list_editable = ('cost',)
    search_fields = ('name', 'used_wood', 'location')
    list_per_page = 25

admin.site.register(Ralization, RalizationAdmin)
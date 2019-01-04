from django.contrib import admin
from .models import Ralization

# @admin.register(Ralization)
class RalizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Ralization, RalizationAdmin)

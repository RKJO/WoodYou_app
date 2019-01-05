from django.contrib import admin
from .models import Assembly

class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly_typ', 'price_m2')
    ordering = ('id',)
    list_display_links = ('id', 'assembly_typ')
    list_editable = ('price_m2',)
    list_per_page = 25

admin.site.register(Assembly, AssemblyAdmin)
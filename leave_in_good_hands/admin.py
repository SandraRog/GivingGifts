from django.contrib import admin
from .models import Institution

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)
    list_filter = ('type',)
    filter_horizontal = ('categories',)

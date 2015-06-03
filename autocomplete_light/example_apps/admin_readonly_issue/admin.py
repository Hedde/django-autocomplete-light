__author__ = 'heddevanderheide'

import autocomplete_light.shortcuts as autocomplete_light

from django import forms
from django.contrib import admin

from .models import ModelX, ModelY


class ModelXAdmin(admin.ModelAdmin):
    pass

admin.site.register(ModelX, ModelXAdmin)


class ModelYAdminForm(forms.ModelForm):
    x = autocomplete_light.ModelChoiceField('ModelXAutocomplete', label="ModelX")


class ModelYAdmin(admin.ModelAdmin):
    form = ModelYAdminForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return 'x'
        return super(ModelYAdmin, self).get_readonly_fields(request, obj=obj)

admin.site.register(ModelY, ModelYAdmin)

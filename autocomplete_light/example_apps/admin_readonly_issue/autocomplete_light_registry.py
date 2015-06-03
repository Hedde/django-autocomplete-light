__author__ = 'heddevanderheide'

import autocomplete_light.shortcuts as autocomplete_light

from .models import ModelX


class ModelXAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['x']

autocomplete_light.register(
    ModelX, ModelXAutocomplete,
    attrs={
        'placeholder': "Enter modelx",
        'data-autocomplete-minimum-characters': 1,
    }
)

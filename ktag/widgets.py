from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class TagInput(forms.TextInput):
    class Media:
        js = []
        try:
            js += [
                settings.STATIC_URL + 'ktag/js/tagify.min.js',
            ]
        except AttributeError:
            print('eeerrr')
            raise ImproperlyConfigured("JS ")

    template_name = 'ktag/ktag_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type

        context['widget']['ktag_args'] = getattr(self, 'ktag_args', None) or {'placeholder': 'write some tags',
                                                                              'delimiters': ',',
                                                                              'whitelist': [],
                                                                              'suggestionsMinChars': 1,
                                                                              'blacklist': [],
                                                                              'maxTags': None}
        return context

from django import forms
from django.core import validators

from ktag.widgets import TagInput


class TagField(forms.CharField):
    widget = TagInput

    def __init__(self, *, place_holder='', delimiters=',', data_list=None,
                 suggestions_chars=1, black_list=None, max_tags=None,
                 max_length=None, min_length=None, strip=True, empty_value='', **kwargs):

        self.max_length = max_length
        self.min_length = min_length
        self.strip = strip
        self.empty_value = empty_value
        super().__init__(**kwargs)
        if min_length is not None:
            self.validators.append(validators.MinLengthValidator(int(min_length)))
        if max_length is not None:
            self.validators.append(validators.MaxLengthValidator(int(max_length)))
        self.validators.append(validators.ProhibitNullCharactersValidator())

        self.delimiters = delimiters
        ktag_args = {}
        ktag_args['placeholder'] = place_holder
        ktag_args['delimiters'] = delimiters
        ktag_args['whitelist'] = data_list if data_list else []
        ktag_args['suggestionsMinChars'] = suggestions_chars
        ktag_args['blacklist'] = black_list if black_list else []
        ktag_args['maxTags'] = max_tags

        setattr(self.widget, 'ktag_args', ktag_args)

    def to_python(self, value):
        value = super().to_python(value)
        return value.split(self.delimiters)

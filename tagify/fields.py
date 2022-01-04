from django import forms
from django.core import validators

from tagify.consts import NameDict
from tagify.widgets import TagInput


class TagField(forms.CharField):
    widget = TagInput

    def __init__(self, *, place_holder='', delimiters=' ', data_list=None,
                 suggestions_chars=1, black_list=None, max_tags=None,
                 max_length=None, min_length=None, strip=True, var_name=None, empty_value='', **kwargs):

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
        tag_args = {}
        tag_args['placeholder'] = place_holder
        tag_args['delimiters'] = delimiters
        tag_args['whitelist'] = data_list if data_list else []
        tag_args['suggestionsMinChars'] = suggestions_chars
        tag_args['blacklist'] = black_list if black_list else []
        tag_args['maxTags'] = max_tags
        setattr(self.widget, 'var_name', var_name)
        setattr(self.widget, 'tag_args', tag_args)

    def to_python(self, value):
        value = super().to_python(value)
        return value.split(self.delimiters)

    def set_var_name(self, value):

        self.widget.var_name = value
        
    def set_tag_args(self, key, value):
        key=NameDict.get(key,key)
        self.widget.tag_args[key] = value

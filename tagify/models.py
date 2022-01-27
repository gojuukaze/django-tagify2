from django.db import models


class TagField(models.Field):

    def __init__(self, place_holder='', delimiters=' ', data_list=None, pattern='', var_name='',
                 suggestions_chars=1, black_list=None, max_tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.delimiters = delimiters
        self.tag_args = {}
        self.tag_args['place_holder'] = place_holder
        self.tag_args['delimiters'] = delimiters
        self.tag_args['data_list'] = data_list
        self.tag_args['suggestions_chars'] = suggestions_chars
        self.tag_args['black_list'] = black_list
        self.tag_args['max_tags'] = max_tags
        self.tag_args['pattern'] = pattern
        self.tag_args['var_name'] = var_name

    def get_internal_type(self):
        return "TextField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = self.delimiters.join(value)
        return super(TagField, self).get_db_prep_value(value, connection, prepared)

    def formfield(self, **kwargs):
        from tagify.fields import TagField as FormTagField
        return super().formfield(form_class=FormTagField, **self.tag_args)

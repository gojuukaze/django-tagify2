import random

from django import forms

from example.models import People
from tagify.fields import TagField


class TagForm(forms.Form):
    languages = TagField(label='languages', place_holder='add a language', delimiters=' ',
                         data_list=['Python', 'Java', 'PHP', 'Golang', 'JavaScript'], initial='Python Golang')


def random_number():
    return [random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), ]


class NumberForm(forms.Form):
    number = TagField(label='number', place_holder='add a number', delimiters=' ',
                      data_list=random_number)


def get_languages():
    return ['Python', 'Java', 'PHP', 'Golang', 'JavaScript']


class PeopleAdminForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['languages'].set_tag_args('data_list',get_languages())

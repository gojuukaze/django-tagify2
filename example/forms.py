import random

from django import forms

from example.models import People
from ktag.fields import TagField


class TagForm(forms.Form):
    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=' ',
                      data_list=['apple', 'banana', 'watermelon', 'orange'], initial='grape coconut')


class PeopleAdminForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=',',
                      data_list=['apple', 'banana', 'watermelon', 'orange'])


def random_number():
    return [random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), ]


class dataListFuncTestForm(forms.Form):
    number = TagField(label='number', place_holder='write your number', delimiters=' ',
                      data_list=random_number)

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
    return [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]


class dataListFuncTestForm(forms.Form):
    number = TagField(label='number', place_holder='write your number', delimiters=' ',
                      data_list=['1', '2', '3', '4'], data_list_func=random_number)

# django-ktag
[![GitHub version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://pypi.org/project/django-ktag/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20V3-blue.svg)](https://github.com/gojuukaze/django-ktag/blob/master/LICENSE)


django tag input field  
[中文README](https://github.com/gojuukaze/django-ktag/blob/master/README.zh.md)

![alt tag](https://github.com/gojuukaze/django-ktag/blob/master/demo.gif?raw=true)

# Credits
* js,css code uses [tagify](https://github.com/yairEO/tagify/blob/master/README.md)

# Requirements

* python3+
* django 2.0+
# Documentation
+ [Installation](#installation)
+ [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Using With Model Admin](#using-with-model-admin)
+ [Field Arguments](#field-arguments)
+ [Example](#example)



# Installation
* download
```shell
pip install django-ktag
or
pip install --index-url https://pypi.org/simple/ django-ktag 
```

* Add 'ktag' application to the INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    'ktag',
]
```
* Make sure `APP_DIRS` is True in TEMPLATES

```python
TEMPLATES = [
    ...
    'APP_DIRS': True,
    ...
]
```

# Usage
## Quick Start
<span id="QuickStart"></span>
**The form class**

Building a form in Django like this:

```python
from django import forms
from ktag.fields import TagField

class TagForm(forms.Form):
    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=' ',
                          data_list=['apple', 'banana', 'watermelon', 'orange'], initial='grape coconut')
```

**The view**

To handle the form we need to instantiate it in the view for the URL where we want it to be published:

```python

from django.http import HttpResponse
from django.shortcuts import render

from example.forms import TagForm

def index(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
           if form.is_valid():
                print(form.cleaned_data['fruits'])
                return HttpResponse(str(form.cleaned_data['fruits']))

    else:
        form = TagForm()
    return render(request, 'index.html', {'form': form})
```

**The template**

The simplest example is:

```python
 <script src="{% static 'ktag/js/tagify.min.js' %}"> </script>
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <br>
    <input type="submit" value="OK" style="font-size: larger">
</form>
```

## Using With Model Admin
ktag is not supported foreign key, so you have to do something by yourself
here is a example:

* Building 2 model
```python
from django.db import models


class People(models.Model):
    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'People'

    name = models.CharField(verbose_name='name', max_length=20)


class PeopleFruits(models.Model):
    class Meta:
        verbose_name = 'People-Fruits'
        verbose_name_plural = 'People-Fruits'

    people_id = models.IntegerField(verbose_name='people_id')
    fruit = models.CharField(verbose_name='fruit', max_length=30)

```
* Building form for admin

```python
from django import forms

from example.models import People
from ktag.fields import TagField

class PeopleAdminForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

    fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=',',
                      data_list=['apple', 'banana', 'watermelon', 'orange'])


```
* Building admin  

the admin in example is a subclass of `ktag.admin.MultipleChoiceAdmin`  

> `MultipleChoiceAdmin` can help you to bind value in admin  
> bind value in `get_object()`  
> save model in `save_model()`  
> *!!! DO NOT FORGET INIT IN `add_view()` !!!*

```python

from django.contrib import admin

from example.forms import PeopleAdminForm
from example.models import People
from ktag.admin import MultipleChoiceAdmin


@admin.register(People)
class PeopleAdmin(MultipleChoiceAdmin):

    form = PeopleAdminForm

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        """
        filter fruits from PeopleFruits
        PeopleFruits.objects.filter(people_id=object_id)
        ...
        """
        # bind value
        self.choice_field_value['fruits'] = "grape,coconut"

        return obj

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        fruits = form.cleaned_data['fruits']
        print(fruits)
        for f in fruits:
            """
            save PeopleFruits
            ...
            if xxx:
                continue
            ...

            """
            PeopleFruits(people_id=obj.id,fruit=f).save()

    def add_view(self, request, form_url='', extra_context=None):
        # !!! do not forget init in add_view !!!
        self.choice_field_value={}
        return super().add_view(request, form_url, extra_context)

```
# Field Arguments

Name                | Type       | Default     | Info
------------------- | ---------- | ----------- | --------------------------------------------------------------------------
place_holder        | string     | ""          | placeholder
delimiters          | string     | ","         | split tags by any of these delimiters. Example: Space or Coma - ", "
data_list           | list|function | []          | an array of tags which they are allowed
black_list          | list       | []          | an array of tags which aren't allowed
max_tags            | int        | None        | max number of tags
suggestions_chars   | int        | 1           | minimum characters to input which shows the sugegstions list


# Example
Run example
```shell
git clone git@github.com:gojuukaze/django-ktag.git  
cd django-ktag
pip install django
python manage.py makemigrations example 
python manage.py migrate   
python manage.py runserver 
```

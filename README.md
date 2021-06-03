# django-tagify2

[![GitHub version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://pypi.org/project/django-tagify2/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20V3-blue.svg)](https://github.com/gojuukaze/django-tagify/blob/master/LICENSE)

django tag input field  
[中文README](https://github.com/gojuukaze/django-tagify2/blob/master/README.zh.md)

![alt tag](https://github.com/gojuukaze/django-tagify2/blob/master/demo.gif?raw=true)

# Credits

* js,css code uses [tagify](https://github.com/yairEO/tagify)

# Requirements

* python3+
* django 2.0+ (maybe 1.x)

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
pip install django-tagify2
or
pip install --index-url https://pypi.org/simple/django-tagify2 
```

* Add 'tagify' application to the INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    'tagify',
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
from tagify.fields import TagField


class TagForm(forms.Form):
    languages = TagField(label='languages', place_holder='add a language', delimiters=' ',
                         data_list=['Python', 'Java', 'PHP', 'Golang', 'JavaScript'], initial='Python Golang')


# or 
def random_number():
    return [random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), random.randint(10, 19), ]


class NumberForm(forms.Form):
    number = TagField(label='number', place_holder='add a number', delimiters=' ',
                      data_list=random_number)


# or 
class TagForm(forms.Form):
    languages = TagField(label='languages', place_holder='add a language', delimiters=' ', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['languages'].set_tag_args('data_list', get_languages())


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
            return HttpResponse(str(form.cleaned_data['languages']))
    else:
        form = TagForm()
    return render(request, 'index.html', {'form': form})


```

**The template**

The simplest example is:

```html

<head>
    {{ form.media }}
</head>
<body>
  <form action="" method="post">
      {% csrf_token %}
      {{ form }}
      <br>
      <input type="submit" value="OK">
  </form>
</body>

```

## Using With Model


```python
from django.db import models

from tagify.models import TagField


class People(models.Model):
    name = models.CharField(max_length=30)
    languages = TagField(verbose_name='languages')

```


# Field Arguments

Name                | Type       | Default     | Info
------------------- | ---------- | ----------- | --------------------------------------------------------------------------
place_holder        | string     | ""          | placeholder
delimiters          | string     | ","         | split tags by any of these delimiters. Example: Space or Coma - ", "
data_list           | list/function | []          | an array of tags which they are allowed
black_list          | list       | []          | an array of tags which aren't allowed
max_tags            | int        | None        | max number of tags
suggestions_chars   | int        | 1           | minimum characters to input which shows the sugegstions list

# Example

Run example

```shell
git clone git@github.com:gojuukaze/django-tagify2.git  
cd django-tagify2
pip install django
python manage.py makemigrations example 
python manage.py migrate   
python manage.py runserver 
```

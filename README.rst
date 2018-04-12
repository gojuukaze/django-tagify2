django-ktag
==========================

-

django tag input field

-

`Home <https://github.com/gojuukaze/django-ktag>`__ | `Documentation <https://github.com/gojuukaze/django-ktag>`__




.. image:: https://github.com/gojuukaze/django-ktag/blob/master/demo.gif?raw=true

Install
----------------------

.. code-block:: shell

    pip install django-ktag

Requirements
----------------------

- python 3+
- django 2+


Quick Start
----------------------

- **The settings**

1. Add 'ktag' application to the INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = [
    ...
    'ktag',
    ]

2. Make sure `APP_DIRS` is True in TEMPLATES

.. code-block:: python

    TEMPLATES = [
    ...
    'APP_DIRS': True,
    ...
    ]


- **The form class**


Building a form in Django like this:

.. code-block:: python

    from django import forms
    from ktag.fields import TagField

    class TagForm(forms.Form):
        fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=' ',
                          data_list=['apple', 'banana', 'watermelon', 'orange'], initial='grape coconut')



- **The view**


To handle the form we need to instantiate it in the view for the URL where we want it to be published:

.. code-block:: python

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


- **The template**


The simplest example is:

.. code-block:: python

    <form action="" method="post">
        {% csrf_token %}
        {{ form }}
        <br>
        <input type="submit" value="OK" style="font-size: larger">
    </form>


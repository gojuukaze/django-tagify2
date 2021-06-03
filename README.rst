django-tagify
=============

|GitHub version| |License: GPL v3|

| django tag input field

.. figure:: https://github.com/gojuukaze/django-tagify/blob/master/demo.gif?raw=true
   :alt: alt tag

   alt tag

Credits
=======

-  js,css code uses `tagify`_

Requirements
============

-  python3+
-  django 2.0+ (maybe 1.x) # Documentation
-  `Installation`_
-  `Usage`_

   -  `Quick Start`_
   -  `Using With Model Admin`_

-  `Field Arguments`_
-  `Example`_

Installation
============

-  download

.. code:: shell

   pip install django-tagify
   or
   pip install --index-url https://pypi.org/simple/ django-tagify

-  Add ‘tagify’ application to the INSTALLED_APPS

.. code:: python

   INSTALLED_APPS = [
       ...
       'tagify',
   ]

-  Make sure ``APP_DIRS`` is True in TEMPLATES

.. code:: python

   TEMPLATES = [
       ...
       'APP_DIRS': True,
       ...
   ]

Usage
=====

Quick Start
-----------

**The form class**

Building a form in Django like this:

.. code:: python

   from django import forms
   from tagify.fields import TagField

   class TagForm(forms.Form):
       fruits = TagField(label='fruits', place_holder='write your fruits', delimiters=' ',
                             data_list=['apple', 'banana', 'watermelon', 'orange'], initial='grape coconut')

**The view**

To handle the form we need to instantiate it in the view for the URL
where we want it to be published:

.. code:: python


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

**The template**

The simplest example is:

.. code:: python

    <script src="{% static 'tagify/js/tagify.min.js' %}"> </script>
   <form action="" method="post">
       {% csrf_token %}
       {{ form }}
       <br>
       <input type="submit" value="OK">
   </form>

Using With Model Admin
----------------------

tagify is not supported foreign key, so you have to do something by
yourself here is a example:

-  Building 2 model \```python from django.db import models

class People(models.Model): class Meta: verbose_name = ‘People’
verbose_name_plural = ‘People’

::

   name = models.CharField(verbose_name='name', max_length=20)

class PeopleFruits(models.Model): class Meta: verbose_name =
‘People-Fruits’ verbose_name_plural = ‘People-Fruits’

::

   people_id = models.IntegerField(verbose_name='people_id')
   fruit = models.CharField(verbose_name='fru

.. _中文README: https://github.com/gojuukaze/django-tagify/blob/master/README.zh.md
.. _tagify: https://github.com/yairEO/tagify
.. _Installation: #installation
.. _Usage: #usage
.. _Quick Start: #quick-start
.. _Using With Model Admin: #using-with-model-admin
.. _Field Arguments: #field-arguments
.. _Example: #example

.. |GitHub version| image:: https://img.shields.io/badge/version-1.0.4-blue.svg
   :target: https://pypi.org/project/django-tagify/
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20V3-blue.svg
   :target: https://github.com/gojuukaze/django-tagify/blob/master/LICENSE
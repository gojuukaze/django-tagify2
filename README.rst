django-tagify2
==============

|GitHub version| |License: GPL v3|

django tag input field

.. figure:: https://github.com/gojuukaze/django-tagify2/blob/master/demo2.gif?raw=true
   :alt: alt tag

   alt tag

Credits
=======

-  js,css code uses `tagify`_

Requirements
============

-  python3+
-  django 2.0+ (maybe 1.x)

Documentation
=============

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

   pip install django-tagify2
   or
   pip install --index-url https://pypi.org/simple/ django-tagify2

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
               return HttpResponse(str(form.cleaned_data['languages']))
       else:
           form = TagForm()
       return render(request, 'index.html', {'form': form})

**The template**

The simplest example is:

.. code:: html


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

Using With Model
----------------

\```python from django.db import models

from tagify.models import TagField

class People(models.Model): name = models.Cha

.. _tagify: https://github.com/yairEO/tagify
.. _Installation: #installation
.. _Usage: #usage
.. _Quick Start: #quick-start
.. _Using With Model Admin: #using-with-model-admin
.. _Field Arguments: #field-arguments
.. _Example: #example

.. |GitHub version| image:: https://img.shields.io/badge/version-1.0.3-blue.svg
   :target: https://pypi.org/project/django-tagify2/
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20V3-blue.svg
   :target: https://github.com/gojuukaze/django-tagify2/blob/master/LICENSE
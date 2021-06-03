from django.db import models

from tagify.models import TagField


class People(models.Model):
    name = models.CharField(max_length=30)
    languages = TagField(verbose_name='languages')

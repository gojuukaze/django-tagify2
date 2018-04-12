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

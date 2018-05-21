from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name='call')
def call(func):
    print(func)
    return func.__call__()
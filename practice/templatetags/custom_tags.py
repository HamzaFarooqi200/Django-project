from django import template

from ..models import Student

register = template.Library()


@register.simple_tag
def cut():
    return Student.objects.count()

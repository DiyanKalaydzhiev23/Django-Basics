from django import template
from django.utils.timezone import now

register = template.Library()


@register.inclusion_tag('common/current_time.html')
def time():
    return {
        'current_time': now(),
    }
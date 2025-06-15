# votre_app/templatetags/custom_filters.py

from django import template
import json

register = template.Library()

@register.filter(name='json_parse')
def json_parse(value):
    """
    Parses a JSON string into a Python object.
    Usage: {{ json_string|json_parse }}
    """
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return {} # Return an empty dictionary or handle error as appropriate

@register.filter(name='make_list')
def make_list(value):
    """
    Creates a list of numbers from 0 up to (but not including) the given value.
    Useful for iterating a specific number of times, e.g., for star ratings.
    Usage: {% for _ in some_number|make_list %}
    """
    try:
        return list(range(int(value)))
    except (ValueError, TypeError):
        return []

@register.filter(name='subtract_from_five')
def subtract_from_five(value):
    """
    Calculates 5 minus the given value and returns a list for iteration.
    Used for displaying empty stars in a 5-star rating system.
    Usage: {% for _ in rating|subtract_from_five %}☆{% endfor %}
    """
    try:
        return list(range(5 - int(value)))
    except (ValueError, TypeError):
        return []


@register.filter
def times(number):
    """
    Creates a list containing `number` elements,
    useful for looping a specific number of times in templates.
    Example: {% for _ in 5|times %}...{% endfor %}
    """
    if isinstance(number, (int, float)):
        return range(int(number))
    return [] # Return an empty list for invalid input
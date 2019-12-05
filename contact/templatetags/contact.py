from django import template

register = template.Library()


@register.filter
def greet(value):
    return 'Hello ' + value + '!'


@register.simple_tag
def greet_me():
    return 'Hello Gabriel!'


@register.simple_tag
def greet_another(name):
    return 'Hello ' + name + '!'


@register.inclusion_tag('contact/last.html')
def last_contact():
    return {}
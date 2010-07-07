from django import template


register = template.Library()


@register.filter
def get_description(hook):
    return hook.description_for_user()
    
@register.filter
def get_value(hook, user):
    return hook.for_user(user)

